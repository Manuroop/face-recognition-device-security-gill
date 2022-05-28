# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uigpEMfd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 454)
        MainWindow.setMinimumSize(QSize(492, 200))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.listWidget = QListWidget(self.frame_6)
        self.listWidget.setObjectName(u"listWidget")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(16)
        self.listWidget.setFont(font1)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setFlow(QListView.TopToBottom)

        self.verticalLayout_4.addWidget(self.listWidget)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(310, 310))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.icon_lbl = QLabel(self.frame_7)
        self.icon_lbl.setObjectName(u"icon_lbl")
        self.icon_lbl.setMinimumSize(QSize(0, 0))
        self.icon_lbl.setMaximumSize(QSize(300, 300))
        self.icon_lbl.setPixmap(QPixmap(u"logo.png"))
        self.icon_lbl.setScaledContents(True)
        self.icon_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_lbl)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 70))
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.show_btn = QPushButton(self.frame_4)
        self.show_btn.setObjectName(u"show_btn")
        self.show_btn.setMinimumSize(QSize(0, 30))
        self.show_btn.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe Print")
        font2.setPointSize(10)
        self.show_btn.setFont(font2)
        self.show_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.show_btn)

        self.searcch_btn = QPushButton(self.frame_4)
        self.searcch_btn.setObjectName(u"searcch_btn")
        self.searcch_btn.setMinimumSize(QSize(0, 30))
        self.searcch_btn.setMaximumSize(QSize(16777215, 30))
        self.searcch_btn.setFont(font2)
        self.searcch_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.searcch_btn)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Allowed people", None))
        self.icon_lbl.setText("")
        self.show_btn.setText(QCoreApplication.translate("MainWindow", u"Show cam", None))
        self.searcch_btn.setText(QCoreApplication.translate("MainWindow", u"Download Intruders", None))
    # retranslateUi

