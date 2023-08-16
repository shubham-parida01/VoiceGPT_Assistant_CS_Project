from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.label = QtWidgets.QLabel(self.frame)
        self.scrollArea = QScrollArea(self.frame)
        self.gif_label=QLabel(self.frame)

        self.frame.setGeometry(0, 0,780,300)
        self.frame.setStyleSheet("background-color: rgb(0,0,0);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label.setGeometry(40, 10,681,240)
        font = QFont("Helvetica")
        self.label.setWordWrap(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("\n"
"font: bold 14pt 'Helvetica';"
"color: rgb(255, 255, 255);"
"background-color: transparent;")

        self.scrollArea.setGeometry(40, 0, 695, 190)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color: transparent;")
        self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar{\n"
"background-color:transparent;\n"
"border:0px solid transparent;\n"
"background:none;}\n"
"QScrollBar:vertical {\n"
"background: rgb(52, 59, 72);\n"
"width: 13px;\n"
"margin: 2px 0px 2px 5px;\n"
"border-radius: 2px;\n"
"border:0px solid transparent; }\n"
"QScrollBar::handle:vertical { background: rgb(0,200,200);\n"
"min-height: 25px;\n"
"border-radius: 2px;\n"
"border:0px solid transparent; }\n"
"QScrollBar::add-line:vertical {\n"
"border: none;\n"
"border:0px solid transparent;\n"
"background: rgb(55, 63, 77);\n"
"height: 0px;\n"
"border-bottom-left-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;}\n"
"QScrollBar::sub-line:vertical {\n"
"border: none;\n"
"border:0px solid transparent;\n"
"background: rgb(55, 63, 77);\n"
"height: 0px;\n"
"border-top-left-radius: 2px;\n"
"border-top-right-radius: 2px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"background: none;\n"
"border:0px solid transparent; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"border:0px solid transparent; }\n"
"QScrollBar:horizontal {\n"
"border: none;\n"
"background: rgb(52, 59, 72);\n"
"height: 20px;\n"
"margin: 2px 0px 2px 5px;\n"
"border-radius: 3px;\n"
"border:0px solid transparent;}\n"
"QScrollBar::handle:horizontal {\n"
"background: rgb(0,200,200);\n"
"min-width: 25px;\n"
"border:0px solid transparent;\n"
"border:none;\n"
"border-radius: 3px}\n"
"QScrollBar::add-line:horizontal {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"width: 0px;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"subcontrol-position: right;\n"
"subcontrol-origin: margin;}\n"
"QScrollBar::sub-line:horizontal {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"width: 0px;\n"
"border-top-left-radius: 3px;\n"
"border-bottom-left-radius: 3px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"background: none;}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;}")

        scroll_widget = QWidget(self.scrollArea)
        self.scrollArea.setWidget(scroll_widget)
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addWidget(self.label)
        scroll_layout.addStretch()
        
        
        self.pushButton.setGeometry(780-35, 0,35, 35)

        self.pushButton.setStyleSheet("border-width:1.3px;\n"
"border-color: rgb(103, 137, 131);\n"
"border-style:solid;\n"
"background-color: rgb(224, 83, 87);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2.setGeometry(315, 170, 50, 50)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(145, 145, 145);\n"
"border-width:2px;\n"
"border-style:solid;\n"
"border-radius:25px")
        self.pushButton_2.setObjectName("pushButton_2")

        
        self.pushButton_3.setGeometry(0, 0, 35, 35)
        self.pushButton_3.setStyleSheet("border-width:1.3px;\n"
"border-color: rgb(103, 137, 131);\n"
"border-style:solid;\n"
"background-color: rgb(29, 91, 121);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4.setGeometry(380, 250, 50, 35)
        self.pushButton_4.setStyleSheet("border-width:1.3px;\n"
"border-color: rgb(103, 137, 131);\n"
"border-style:solid;\n"
"background-color: rgb(29, 91, 121);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.hide()

        self.gif_path = "Loading_icon.gif"
        self.anim = QMovie(self.gif_path)
        
        self.gif_label.setGeometry(310, 140,170,170)
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.gif_label.setMovie(self.anim)
        self.anim.start()
        
        self.label_2=QLabel(self.frame)
        self.label_2.setGeometry(350, 190,60,100)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet("background-image : url(mic_2.png);")
        self.label_2.hide()
        
        self.label_3=QLabel(self.frame)
        self.label_3.setGeometry(310, 180,154,114)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.path= "speaker.gif"
        self.speak = QMovie(self.path)
        self.label_3.setMovie(self.speak)
        self.speak.start()
        self.label_3.hide()

        self.pushButton_2.setGeometry(self.gif_label.geometry())
        self.pushButton_2.setText("")
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.setStyleSheet("background-color: transparent; border: none;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Hi! What can I do for you? \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nwwwwww"))
        self.pushButton_3.setText(_translate("MainWindow", "?"))
        self.pushButton_4.setText(_translate("MainWindow","CLOSE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
