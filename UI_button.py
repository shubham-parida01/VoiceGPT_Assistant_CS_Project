import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import socket
import speech_recognition as sr
import pyttsx3
import platform
from gtts import gTTS
from PyQt5.QtGui import QMovie
import threading
from threading import Thread
import os
import pyjokes
import datetime
import cv2
import time

#from main_window import Ui_MainWindow
from splash_ui import Ui_SplashScreen
import get_temp
import maps
import ChatGpt
import spotify_windows as sw
import spotify_mac as sm
import web_search as ws
import Open_apps as oa
from tr import Ui_MainWindow

counter = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.splash = Ui_SplashScreen()
        self.splash.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)  # removes titlebar
        self.setAttribute(Qt.WA_TranslucentBackground)  # "

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.splash.frame.setGraphicsEffect(self.shadow)

        self.timer = QTimer()  # timer for progress bar
        self.timer.timeout.connect(self.update)
        self.timer.start(20)  # timeout for 20 milliseconds
        QtCore.QTimer.singleShot(0, lambda: self.splash.label_2.setText("Shubham"))
        QtCore.QTimer.singleShot(2000, lambda: self.splash.label_2.setText("Bhavya"))#changes text after given time
        QtCore.QTimer.singleShot(3000, lambda: self.splash.label_2.setText("Ashmit"))

        self.show()
        self.main = MainWindow()

    def check_internet_connection(self):#checks for internet
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except socket.error:
            return False

    def update(self):#updates the pprogress bar
        global counter
        self.splash.progressBar.setValue(counter)
        if counter > 100:  
            self.timer.stop()
            self.close()  # closes splashscreen
            if self.check_internet_connection():
                self.main.show()
            else:
                self.main.show()
                self.main.main.pushButton_2.setEnabled(False)
                self.main.text = "No internet connection"
        counter += 1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.main = Ui_MainWindow()
        self.main.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(780, 300)
        self.adjustSize()

        self.shadow = QGraphicsDropShadowEffect(self) #adds shadow to window
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0,60))
        self.main.frame.setGraphicsEffect(self.shadow)

        self.index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.display)
        self.timer.start(100)

        self.main.pushButton.pressed.connect(self.closewindow)
        self.main.pushButton_2.pressed.connect(self.listening)
        self.main.pushButton_3.pressed.connect(self.help)
        self.main.pushButton_4.pressed.connect(self.close_commands)
        self.text = "Hi! What can I do for you?"

        layout=QStackedLayout()
        layout.addWidget(self.main.gif_label)
        layout.addWidget(self.main.pushButton_2)
        layout.setCurrentIndex(1)
        self.setLayout(layout)
        #self.main.anim.stop()
        self.main.gif_label.show()

    def gif_start(self):
        self.main.anim.start()

    def close_commands(self):
        self.main.scrollArea.setGeometry(40, 0, 695, 190)
        self.main.pushButton_4.hide()
        self.main.gif_label.show()
        self.main.pushButton_2.show()
        self.text="Hi! What can I do for you?"
        #self.main.label.setText("Hi! What can I do for you?")
        
    def listening(self):
        self.main.gif_label.hide()
        self.main.label_2.show()
        self.text = "Listening..."
        thread = threading.Thread(target=self.speech_rec)
        thread.start()

    def help(self):#help button
        self.main.pushButton_4.show()
        self.main.gif_label.hide()
        self.main.pushButton_2.hide()
        self.main.scrollArea.setGeometry(40, 0, 695, 220)
        self.text= """COMMANDS
        Maps: Direction to <destination>
        Temperature: Temprature in <location>
        Music: Play <song_name>
        Google: Search <your_query>
        Joke: Tell me a joke 
        Time: Whats the time
        Date: Whats the date
        Open apps:Open <app_name>
        Click a Photo: Take my photo
        ChatGpt: <your_query>"""
        self.main.label.setText(self.text)

    def closewindow(self):#close button
        exit()

    def speech_rec(self):
        self.gif_start()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = r.listen(source,timeout=10)
                time.sleep(3)
                self.main.label_2.hide()
                self.main.gif_label.hide()
                self.main.pushButton_2.hide()
                self.main.label_3.show()

            except sr.WaitTimeoutError:
                self.text="Try Again!"
                self.main.label_2.hide()
                self.main.gif_label.show()
                self.main.pushButton_2.show()
                return None
        audio_rec=r.recognize_google(audio).capitalize()
        self.text =f"You said: {audio_rec}"
        try:
            b = audio_rec.split()
            c = len(b[0])
            print(audio_rec)
            if audio_rec.startswith(("direction to","Direction to","directions to","Directions to")):
                maps.open_maps(audio_rec[c + 2::])

            elif audio_rec.startswith(("Temperature in")):
                temperature = get_temp.get_current_temperature(audio_rec[c + 3::])
                self.text = f"The Temperature in{(audio_rec[c + 3::]).capitalize()} is {temperature} Celsius."
                self.main.label.setText(self.text)
                self.speaker(self.text)
            elif audio_rec.startswith(("Play")) and self.check_os() == "Windows":
                sw.music_play(self.text[c + 1::])
                self.text = f"Playing {self.text[c + 1::]}"
                self.main.label.setText(self.text)

            elif audio_rec.startswith(("Play")) and self.check_os() == "macOS":
                sm.play_song(self.text[c + 1::])
                self.text = f"Playing {self.text[c + 1::]}"
                self.main.label.setText(self.text)

            elif audio_rec.startswith(("Search")):
                ws.search_on_google(audio_rec[c + 1::])

            elif audio_rec in ("Tell me a joke"):
                text = pyjokes.get_joke("en","neutral")
                self.main.label.setText(self.text)
                self.speaker(text)

            elif audio_rec.startswith(("Open")):
                a = audio_rec[c + 1::]
                oa.open_application(audio_rec[c + 1::])
                self.text = f"Opening {a.capitalize()}"
                self.main.label.setText(self.text)
                self.speaker(self.text)

            elif audio_rec in ("What's the time","Tell me the time"):
                Time = datetime.datetime.now().strftime("%H:%M:%S")   
                self.text=f"Current time is {Time}"
                self.speaker(self.text)

            elif audio_rec in ("What's the date""Tell me the date","Today's date"):
                date = datetime.date.today()  
                self.text=f"Today's date is {date}"
                self.speaker(self.text)
            
            elif audio_rec in ("Take my photo","Camera"):
                c=1
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    self.text="Unable to access the camera"
                ret, frame = cap.read()
                if not ret:
                    self.text="Failed to capture your picture"
                cap.release()
                while True:
                    file_path = f"0{str(c)}.jpg"
                    if not os.path.exists(file_path):
                        cv2.imwrite(file_path, frame)
                        self.text=(f"Image captured and saved as '{file_path}'")
                        break
                    c+=1


            else:
                answer = ChatGpt.chat_gpt(audio_rec)
                self.text = answer
                self.main.label.setText(self.text)
                self.speaker(self.text)
            
        except sr.UnknownValueError:
            self.text = "Try Again!"
            self.main.label.repaint()
            
        except sr.RequestError as e:
            self.text = "Could not request results from Google Speech Recognition service" + str(e)
        self.main.scrollArea.setGeometry(40, 0, 695, 135)
        self.main.label_2.hide()
        self.main.gif_label.show()
        self.main.pushButton_2.show()

    def display(self):
        self.main.label.setText(self.text)
        self.main.label.repaint()

    def check_os(self):#checks os 
        system = platform.system()
        if system == "Windows":
            return "Windows"
        elif system == "Darwin":
            return "macOS"
        else:
            return "Unknown"

    def speaker(self, s):#
        if self.check_os() == "Windows":
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", 150)
            self.engine.setProperty("volume", 1)
            self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
            self.engine.say(s)
            self.engine.runAndWait()
        elif self.check_os() == "macOS":
            from pydub import AudioSegment
            from pydub.playback import play
            tts = gTTS(s, lang='en')
            temp_file = "temp.mp3"
            tts.save(temp_file)
            audio = AudioSegment.from_file(temp_file, format="mp3")
            play(audio)
            os.remove(temp_file)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    '''main=MainWindow()
    main.show()'''
    sys.exit(app.exec())
