from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QToolButton, 
QRadioButton, QComboBox, QProgressBar, QFileDialog, QMessageBox)
from PySide6.QtCore import Slot, Signal, QObject
from ui_main import Ui_MainWindow
from csv import reader
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from threading import Thread

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.downloadAddress = ""
        self.saveAddress = ""
        self.counter = 1
        self.rowNumber = 0

        self.ui.downloadAddressSelector.clicked.connect(self.downloadAddressSelect)
        self.ui.downloadAddress.textChanged.connect(self.downloadAddressChanged)    #注意与textEdited的区别
        self.ui.downloadAddressConfirm.clicked.connect(self.readCsvFile)

        self.ui.addressColumnSelector.currentIndexChanged.connect(self.setAddressColumn)

        self.ui.buttonGroup.buttonClicked.connect(self.buttonGroupClicked)
        self.ui.tableNamingSelector.currentIndexChanged.connect(self.setTableNaming)  #此处的selector指下拉框，而非toolbutton
        self.ui.customNamingSelector.currentIndexChanged.connect(self.setCustomNaming)

        self.ui.saveAddressSelector.clicked.connect(self.saveAddressSelect)
        self.ui.saveAddress.textChanged.connect(self.saveAddressChanged)
        
        self.ui.download.clicked.connect(self.download)

        mySignals.progressBarRefresh.connect(self.refreshProgressBar)
        mySignals.httpErrorWarning.connect(self.httpError)
        mySignals.urlErrorWarning.connect(self.urlError)

    @Slot()
    def downloadAddressSelect(self):
        path, _  = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "d:\\",
            "文件类型 (*.csv)"
        )
        if path != "":
            self.downloadAddress = path
            self.ui.downloadAddress.setText(self.downloadAddress)

    @Slot()
    def downloadAddressChanged(self):
        self.downloadAddress = self.ui.downloadAddress.text()
        if self.downloadAddress != "":
            self.ui.downloadAddressConfirm.setEnabled(True)
        else:
            self.ui.downloadAddressConfirm.setEnabled(False)

    @Slot()
    def readCsvFile(self):
        try:
            self.csvFile = reader(open(self.downloadAddress, 'r', encoding='utf-8-sig'))
            self.tableHead = self.getTableHead()

            self.ui.addressColumnSelector.clear()
            self.ui.addressColumnSelector.addItems(self.tableHead)
            self.ui.tableNamingSelector.clear()
            self.ui.tableNamingSelector.addItems(self.tableHead)
            self.ui.customNamingSelector.clear()
            self.ui.customNamingSelector.addItems(["数字递增","数字递减"])
        except FileNotFoundError:
            QMessageBox.warning(
                self,
                "警告",
                "文件路径错误"
            )
    
    def getTableHead(self):
        return next(self.csvFile)

    @Slot()
    def setAddressColumn(self):
        self.addressColumn = self.ui.addressColumnSelector.currentIndex()

    def getAddressColumn(self):
        return self.addressColumn

    @Slot()
    def buttonGroupClicked(self):
        if self.ui.tableNaming.isChecked():
            self.ui.tableNamingSelector.setEnabled(True)
            self.ui.customNamingSelector.setEnabled(False)

        if self.ui.customNaming.isChecked():
            self.ui.tableNamingSelector.setEnabled(False)
            self.ui.customNamingSelector.setEnabled(True)
    
    @Slot()
    def setTableNaming(self):
        self.tableNaming = self.ui.tableNamingSelector.currentIndex()

    def getTableNaming(self):
        return self.tableNaming
    
    @Slot()
    def setCustomNaming(self):
        self.customNaming = self.ui.customNamingSelector.currentIndex()

    def getCustomNaming(self):
        return self.customNaming

    @Slot()
    def saveAddressSelect(self):
        path = QFileDialog.getExistingDirectory(self, "选择存储路径")
        if path != "":
            self.saveAddress = path
            self.ui.saveAddress.setText(self.saveAddress)

    @Slot()
    def saveAddressChanged(self):
        self.saveAddress = self.ui.saveAddress.text()

        if self.saveAddress != "" and self.ui.buttonGroup.checkedButton() != None:
            self.ui.download.setEnabled(True)
        else:
            self.ui.download.setEnabled(False)
    
    def setRowNumber(self):
        tmpCsvFile = reader(open(self.downloadAddress, 'r', encoding='utf-8-sig'))
        counter = 0
        for i in tmpCsvFile:
            counter += 1
        self.rowNumber = counter

    def getRowNumber(self):
        return self.rowNumber
    
    @Slot()
    def download(self):

        def downloadThread():
            while True:
                try:
                    self.toNextRow()
                    filename = self.getFileNameWithoutSuffix() + self.getFileSuffix()
                    fileFullPath = self.saveAddress + "\\" + filename
                    url = urlopen(self.getUrl())
                    with open(fileFullPath, 'wb') as file:
                        buffer = url.read()
                        file.write(buffer)
                        file.flush
                    # 注意此处不能由槽函数自行访问counter和rownumber并对progressbar的value赋值，
                    # 因为此处有两个线程，主线程访问counter时可能子线程已经开始处理下一个文件，counter发生改变
                    mySignals.progressBarRefresh.emit(round(self.counter / (self.getRowNumber() - 1) * 100))
                    self.counter += 1
                except StopIteration:
                    self.reInitialization()
                    break
                except HTTPError as ex:
                    mySignals.httpErrorWarning.emit(
                        "HTTP Error %s: %s" % (ex.code, ex.msg), "第%s行" % self.counter)
                    self.reInitialization()
                    return
                except URLError as ex:
                    mySignals.httpErrorWarning.emit(
                        "Urlopen Error: %s" % ex.reason, "第%s行" % self.counter)
                    self.reInitialization()
                    return        

        self.setRowNumber()
        thread = Thread(target = downloadThread)
        thread.start()

    @Slot()
    def refreshProgressBar(self, num):
        self.ui.progressBar.setValue(num)
    
    @Slot()
    def httpError(self, msg, inf):
        QMessageBox.warning(
                        self,
                        "警告",
                        inf + "\n" + msg
                    )
    
    @Slot()
    def urlError(self, msg, inf):
        QMessageBox.warning(
                        self,
                        "警告",
                        inf + "\n" + msg
                    )

    def reInitialization(self):
        self.csvFile = reader(open(self.downloadAddress, 'r', encoding='utf-8-sig'))
        self.getTableHead() #跳过表头，使下载从第二行开始
        self.counter = 1

    def toNextRow(self):
        self.currentRow = next(self.csvFile)
    
    def getCurrentRow(self):
        return self.currentRow

    def getUrl(self):
        return self.getCurrentRow()[self.getAddressColumn()]

    def getFileSuffix(self):
        SUFFIXLIB = [".pdf",".doc",".docx",".png",".PNG",".jpg",".JPG",".jpeg"]
        for suffix in SUFFIXLIB:
            if self.getUrl().find(suffix) != -1:
                return suffix
        raise Exception("Unsupported file suffix")
    
    def getFileNameWithoutSuffix(self):
        if self.ui.tableNaming.isChecked():
            return self.getCurrentRow()[self.getTableNaming()]
        else:
            if self.getCustomNaming() == 0:
                return str(self.counter)
            else:
                return str(self.getRowNumber() - self.counter)
    
class MySignals(QObject):
    progressBarRefresh = Signal(int)
    httpErrorWarning = Signal(str, str)
    urlErrorWarning = Signal(str, str)

if __name__ == "__main__":
    app = QApplication([])
    mySignals = MySignals()
    downloader = MainWindow()
    downloader.show()
    app.exec()