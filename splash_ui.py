from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 408)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        SplashScreen.setWindowFlag(Qt.FramelessWindowHint)
        SplashScreen.setAttribute(Qt.WA_TranslucentBackground)

        self.frame.setGeometry(QtCore.QRect(0, 0, 681, 411))
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(46, 79, 79, 255), stop:1 rgba(32, 46, 83, 255));\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        x,y,w,h=self.frame.geometry().getRect()

        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect((w-491)//2, h-100, 491, 7))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    background-color: rgb(220, 220, 220);\n"
"    border-style:none;\n"
"    border-radius:3px;\n"
"    font: 8pt ;\n"
"    text-align:center;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:3px;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(194, 118, 100, 255), stop:1 rgba(228, 201, 136, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.label = QtWidgets.QLabel(self.frame)#creaetd by
        self.label.setGeometry(QtCore.QRect(530, h-23, 71, 16))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"font: 8pt \"Impact\";\n"
"color: rgb(140, 140, 140);")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)#Names
        self.label_2.setGeometry(QtCore.QRect(w-70, h-23, 61, 16))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(203, 203, 203);\n"
"\n"
"font: 8pt \"Impact\";")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame)#CS Project
        self.label_3.setGeometry(QtCore.QRect((w-321)//2, (100), 321, 51))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 25pt \"Montserrat SemiBold\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(182, 182, 182, 255));")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame)#loading...
        self.label_4.setGeometry(QtCore.QRect((w-71)//2, 320, 71, 20))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(212, 212, 212);")
        self.label_4.setObjectName("label_4")
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label.setText(_translate("SplashScreen", "CREATED BY:"))
        self.label_2.setText(_translate("SplashScreen", "asfas"))
        self.label_3.setText(_translate("SplashScreen", "CS PROJECT"))
        self.label_4.setText(_translate("SplashScreen", "Loading..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
