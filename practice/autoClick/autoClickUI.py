# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autoClickUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(966, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 80, 86, 12))
        self.mouseButton = QPushButton(self.centralwidget)
        self.mouseButton.setObjectName(u"mouseButton")
        self.mouseButton.setEnabled(True)
        self.mouseButton.setGeometry(QRect(230, 130, 132, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mouseButton.sizePolicy().hasHeightForWidth())
        self.mouseButton.setSizePolicy(sizePolicy1)
        self.keyBotton = QPushButton(self.centralwidget)
        self.keyBotton.setObjectName(u"keyBotton")
        self.keyBotton.setEnabled(True)
        self.keyBotton.setGeometry(QRect(450, 130, 118, 31))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QRect(410, 180, 181, 169))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.keyClickTime = QSpinBox(self.layoutWidget)
        self.keyClickTime.setObjectName(u"keyClickTime")
        self.keyClickTime.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.keyClickTime)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.keyChar = QLineEdit(self.layoutWidget)
        self.keyChar.setObjectName(u"keyChar")
        self.keyChar.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.keyChar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.keyClickInv = QDoubleSpinBox(self.layoutWidget)
        self.keyClickInv.setObjectName(u"keyClickInv")
        self.keyClickInv.setEnabled(False)
        self.keyClickInv.setDecimals(3)
        self.keyClickInv.setMinimum(0.001000000000000)
        self.keyClickInv.setMaximum(100.000000000000000)
        self.keyClickInv.setSingleStep(0.001000000000000)

        self.horizontalLayout_6.addWidget(self.keyClickInv)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.startMouseBotton = QPushButton(self.centralwidget)
        self.startMouseBotton.setObjectName(u"startMouseBotton")
        self.startMouseBotton.setGeometry(QRect(220, 390, 101, 31))
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setEnabled(True)
        self.layoutWidget1.setGeometry(QRect(200, 180, 181, 169))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.mouseClickTime = QSpinBox(self.layoutWidget1)
        self.mouseClickTime.setObjectName(u"mouseClickTime")
        self.mouseClickTime.setEnabled(False)
        self.mouseClickTime.setMinimum(1)
        self.mouseClickTime.setMaximum(999999)

        self.horizontalLayout.addWidget(self.mouseClickTime)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.mouseLeftorRight = QComboBox(self.layoutWidget1)
        self.mouseLeftorRight.addItem("")
        self.mouseLeftorRight.addItem("")
        self.mouseLeftorRight.setObjectName(u"mouseLeftorRight")
        self.mouseLeftorRight.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.mouseLeftorRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.mouseClickInv = QDoubleSpinBox(self.layoutWidget1)
        self.mouseClickInv.setObjectName(u"mouseClickInv")
        self.mouseClickInv.setEnabled(False)
        self.mouseClickInv.setDecimals(3)
        self.mouseClickInv.setMinimum(0.001000000000000)
        self.mouseClickInv.setMaximum(100.000000000000000)
        self.mouseClickInv.setSingleStep(0.001000000000000)

        self.horizontalLayout_2.addWidget(self.mouseClickInv)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.startKeyBotton = QPushButton(self.centralwidget)
        self.startKeyBotton.setObjectName(u"startKeyBotton")
        self.startKeyBotton.setGeometry(QRect(440, 390, 111, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 966, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.keyBotton.clicked["bool"].connect(self.keyClickTime.setDisabled)
        self.mouseButton.clicked["bool"].connect(self.keyClickTime.setEnabled)
        self.mouseButton.clicked["bool"].connect(self.keyChar.setEnabled)
        self.mouseButton.clicked["bool"].connect(self.keyClickInv.setEnabled)
        self.keyBotton.clicked["bool"].connect(self.keyChar.setDisabled)
        self.keyBotton.clicked["bool"].connect(self.keyClickInv.setDisabled)
        self.mouseButton.clicked["bool"].connect(self.mouseClickTime.setDisabled)
        self.mouseButton.clicked["bool"].connect(self.mouseLeftorRight.setDisabled)
        self.mouseButton.clicked["bool"].connect(self.mouseClickInv.setDisabled)
        self.keyBotton.clicked["bool"].connect(self.mouseClickTime.setEnabled)
        self.keyBotton.clicked["bool"].connect(self.mouseLeftorRight.setEnabled)
        self.keyBotton.clicked["bool"].connect(self.mouseClickInv.setEnabled)
        self.mouseButton.clicked["bool"].connect(self.startMouseBotton.setDisabled)
        self.mouseButton.clicked["bool"].connect(self.startKeyBotton.setEnabled)
        self.keyBotton.clicked["bool"].connect(self.startKeyBotton.setDisabled)
        self.keyBotton.clicked["bool"].connect(self.startMouseBotton.setEnabled)
        self.startMouseBotton.clicked.connect(MainWindow.startMouseClickslot)
        self.startKeyBotton.clicked.connect(MainWindow.startKeyClickslot)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoClickUI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"autoClick", None))
        self.mouseButton.setText(QCoreApplication.translate("MainWindow", u"mouseAutoClick", None))
        self.keyBotton.setText(QCoreApplication.translate("MainWindow", u"keyAutoClick", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u6309\u6b21\u6570\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u6309\u5b57\u6bcd\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u95f4\u9694/s:", None))
        self.startMouseBotton.setText(QCoreApplication.translate("MainWindow", u"startMouse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6b21\u6570\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u952e/\u53f3\u952e\uff1a", None))
        self.mouseLeftorRight.setItemText(0, QCoreApplication.translate("MainWindow", u"left", None))
        self.mouseLeftorRight.setItemText(1, QCoreApplication.translate("MainWindow", u"right", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u95f4\u9694/s:", None))
        self.startKeyBotton.setText(QCoreApplication.translate("MainWindow", u"startKey", None))
    # retranslateUi

