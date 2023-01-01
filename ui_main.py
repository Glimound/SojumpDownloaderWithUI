# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(383, 347)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.downloadAddress = QLineEdit(self.centralwidget)
        self.downloadAddress.setObjectName(u"downloadAddress")
        self.downloadAddress.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(17)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.downloadAddress.sizePolicy().hasHeightForWidth())
        self.downloadAddress.setSizePolicy(sizePolicy1)
        self.downloadAddress.setFont(font)
        self.downloadAddress.setMouseTracking(True)

        self.horizontalLayout.addWidget(self.downloadAddress)

        self.downloadAddressSelector = QToolButton(self.centralwidget)
        self.downloadAddressSelector.setObjectName(u"downloadAddressSelector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.downloadAddressSelector.sizePolicy().hasHeightForWidth())
        self.downloadAddressSelector.setSizePolicy(sizePolicy2)
        self.downloadAddressSelector.setFont(font)

        self.horizontalLayout.addWidget(self.downloadAddressSelector)

        self.downloadAddressConfirm = QPushButton(self.centralwidget)
        self.downloadAddressConfirm.setObjectName(u"downloadAddressConfirm")
        self.downloadAddressConfirm.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.downloadAddressConfirm.sizePolicy().hasHeightForWidth())
        self.downloadAddressConfirm.setSizePolicy(sizePolicy3)
        self.downloadAddressConfirm.setMinimumSize(QSize(20, 0))
        self.downloadAddressConfirm.setFont(font)

        self.horizontalLayout.addWidget(self.downloadAddressConfirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 30)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setKerning(True)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.addressColumnSelector = QComboBox(self.centralwidget)
        self.addressColumnSelector.setObjectName(u"addressColumnSelector")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.addressColumnSelector.sizePolicy().hasHeightForWidth())
        self.addressColumnSelector.setSizePolicy(sizePolicy4)
        self.addressColumnSelector.setFont(font)

        self.horizontalLayout_6.addWidget(self.addressColumnSelector)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableNaming = QRadioButton(self.groupBox_4)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.tableNaming)
        self.tableNaming.setObjectName(u"tableNaming")
        self.tableNaming.setFont(font)

        self.horizontalLayout_2.addWidget(self.tableNaming)

        self.tableNamingSelector = QComboBox(self.groupBox_4)
        self.tableNamingSelector.setObjectName(u"tableNamingSelector")
        self.tableNamingSelector.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.tableNamingSelector)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.customNaming = QRadioButton(self.groupBox_4)
        self.buttonGroup.addButton(self.customNaming)
        self.customNaming.setObjectName(u"customNaming")
        self.customNaming.setFont(font)

        self.horizontalLayout_3.addWidget(self.customNaming)

        self.customNamingSelector = QComboBox(self.groupBox_4)
        self.customNamingSelector.setObjectName(u"customNamingSelector")
        self.customNamingSelector.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.customNamingSelector)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.groupBox_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.saveAddress = QLineEdit(self.centralwidget)
        self.saveAddress.setObjectName(u"saveAddress")
        self.saveAddress.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(11)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.saveAddress.sizePolicy().hasHeightForWidth())
        self.saveAddress.setSizePolicy(sizePolicy5)
        self.saveAddress.setFont(font)
        self.saveAddress.setMouseTracking(True)

        self.horizontalLayout_5.addWidget(self.saveAddress)

        self.saveAddressSelector = QToolButton(self.centralwidget)
        self.saveAddressSelector.setObjectName(u"saveAddressSelector")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.saveAddressSelector.sizePolicy().hasHeightForWidth())
        self.saveAddressSelector.setSizePolicy(sizePolicy6)
        self.saveAddressSelector.setFont(font)

        self.horizontalLayout_5.addWidget(self.saveAddressSelector)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_5.addWidget(self.progressBar)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.download = QPushButton(self.centralwidget)
        self.download.setObjectName(u"download")
        self.download.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.download.sizePolicy().hasHeightForWidth())
        self.download.setSizePolicy(sizePolicy7)
        self.download.setFont(font)

        self.horizontalLayout_7.addWidget(self.download)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u95ee\u5377\u661f\u4e0b\u8f7d\u5668", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"csv\u6587\u4ef6\u5730\u5740", None))
        self.downloadAddressSelector.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.downloadAddressConfirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5730\u5740\u6240\u5728\u5217", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6587\u4ef6\u547d\u540d\u65b9\u5f0f", None))
        self.tableNaming.setText(QCoreApplication.translate("MainWindow", u"\u8868\u683c\u4fe1\u606f", None))
        self.customNaming.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6587\u4ef6\u4fdd\u5b58\u5730\u5740", None))
        self.saveAddressSelector.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
    # retranslateUi

