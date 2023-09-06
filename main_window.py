from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(790,310)
        MainWindow.adjustSize()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.main_close = QtWidgets.QPushButton(self.frame)
        self.listening_button = QtWidgets.QPushButton(self.frame)
        self.help_button = QtWidgets.QPushButton(self.frame)
        self.help_close = QtWidgets.QPushButton(self.frame)
        self.main_label = QtWidgets.QLabel(self.frame)
        self.scrollArea = QScrollArea(self.frame)
        self.gif_label=QLabel(self.frame)
        self.speaker_label=QLabel(self.frame)#speaker animation
        self.mic_label=QLabel(self.frame)#mic image

        self.frame.setGeometry(0, 0,780,300)
        self.frame.setStyleSheet("background-color: rgb(0,0,0);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        x,y,w,h=self.frame.geometry().getRect()
        self.main_label.setGeometry(40, 5,681,240)#main main_label
        font = QFont("Montserrat Black")
        self.main_label.setWordWrap(True)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.main_label.setObjectName("main_label")
        self.main_label.setStyleSheet("\n"
"font: 14pt;"
"color: rgb(255, 255, 255);"
"background-color: transparent;")

        self.scrollArea.setGeometry(self.main_label.geometry())#text area
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
"border:0px solid transparent; }\n")

        scroll_widget = QWidget(self.scrollArea)
        self.scrollArea.setWidget(scroll_widget)
        scroll_layout = QVBoxLayout(scroll_widget)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_layout.addWidget(self.main_label)
        scroll_layout.addStretch()

        self.main_close.setGeometry(w-35, 0,35, 35)#main window close
        self.main_close.setStyleSheet("border-width:1.3px;\n"
"border-color: rgb(103, 137, 131);\n"
"border-style:solid;\n"
"background-color: rgb(224, 83, 87);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")
        self.main_close.setObjectName("main_close")
        
        self.listening_button.setStyleSheet("background-color: transparent ; border: none; border-radius:20px")
        self.listening_button.setObjectName("listening_button")
        self.listening_button.setGeometry((w-100)//2, (h-100),100,100)#listening_button geometry
        self.gif_path = "Loading_icon.gif"
        self.anim = QMovie(self.gif_path)
        self.gif_label.setGeometry((w-100)//2, (h-100),100,100)#main button animation
        self.gif_label.setStyleSheet("border-radius:10px")
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.gif_label.setMovie(self.anim)
        self.anim.start()

        self.help_button.setGeometry(0, 0, 35, 35)#help button
        self.help_button.setStyleSheet("border-width:1.3px;\n"
"border-color: rgb(103, 137, 131);\n"
"border-style:solid;\n"
"background-color: rgb(29, 91, 121);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")
        self.help_button.setObjectName("help_button")
        
        self.help_close.setGeometry((w-50)//2, 250, 50, 35)#help close button
        self.help_close.setStyleSheet("border-width:1.3px;\n"
"border-color: rgb(103, 137, 131);\n"
"border-style:solid;\n"
"background-color: rgb(29, 91, 121);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")
        self.help_close.setObjectName("help_close")
        self.help_close.hide()

        self.mic_label.setGeometry((w-60)//2, 190,60,100)
        self.mic_label.setAlignment(Qt.AlignCenter)
        self.mic_label.setStyleSheet("background-image : url(mic_2.png);")
        self.mic_label.hide()
        
        self.speaker_label.setGeometry((w-154)//2, 180,154,114)
        self.speaker_label.setAlignment(Qt.AlignCenter)
        self.path= "speaker.gif"
        self.speak = QMovie(self.path)
        self.speaker_label.setMovie(self.speak)
        self.speak.start()
        self.speaker_label.hide()

        self.listening_button.setFocusPolicy(Qt.NoFocus)#on top

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_close.setText(_translate("MainWindow", "X"))
        self.main_label.setText(_translate("MainWindow", "Hi! What can I do for you?"))
        self.help_button.setText(_translate("MainWindow", "?"))
        self.help_close.setText(_translate("MainWindow","CLOSE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
