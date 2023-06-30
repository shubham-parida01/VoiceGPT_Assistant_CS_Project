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

import os
import pyjokes
import datetime
import cv2

from ui_popup import Ui_MainWindow
from ui_splash import Ui_SplashScreen
import get_temp
import maps
import ChatGpt
import spotify_windows as sw
import spotify_mac as sm
import web_search as ws
import Open_apps as oa

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
        self.timer.start(20)  # timeout for 50 milliseconds

        QtCore.QTimer.singleShot(1600, lambda: self.splash.label_2.setText("Bhavya"))
        QtCore.QTimer.singleShot(2600, lambda: self.splash.label_2.setText("Ashmit"))

        self.show()
        self.main = MainWindow()

    def check_internet_connection(self):
        try:
            # Attempt to connect to a well-known website (e.g., Google DNS server)
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except socket.error:
            return False

    def update(self):
        global counter  # counter for progress bar
        self.splash.progressBar.setValue(counter)
        if counter > 100:  # upto 100% progress
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
        self.setMinimumSize(680, 220)
        self.adjustSize()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.main.frame.setGraphicsEffect(self.shadow)

        self.index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.display)
        self.timer.start(100)

        self.main.pushButton.pressed.connect(self.closewindow)
        self.main.pushButton_2.pressed.connect(self.listening)
        self.text = "Hi! What can I do for you?"

    def closewindow(self):
        self.close()

    def display(self):
        self.main.label.setText(self.text)

    def listening(self):
        self.main.label.setText("Listening...")
        self.main.label.repaint()  # Update the label immediately
        self.speech_rec()

    def speech_rec(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            self.text = r.recognize_google(audio)
            b = self.text.split()
            c = len(b[0])
            print(self.text)
            if self.text.startswith(("direction to","Direction to","directions to","Directions to")):
                maps.open_maps(self.text[c + 2::])

            elif self.text.startswith(("Temperature in", "temperature in")):
                temperature = get_temp.get_current_temperature(self.text[c + 3::])
                self.text = f"The temperature in{self.text[c + 3::]} is {temperature} Celsius."
                self.main.label.setText(self.text)
                self.main.label.repaint()
                self.speaker(self.text)

            elif self.text.startswith(("Play", "play")) and self.check_os() == "Windows":
                song = self.text[c + 1::]
                sw.music_play(self.text[c + 1::])
                self.text = f"Playing {song}"
                self.main.label.setText(self.text)
                self.main.label.repaint()
                self.speaker(self.text)

            elif self.text.startswith(("Play", "play")) and self.check_os() == "macOS":
                song = self.text[c + 1::]
                sm.play_song(self.text[c + 1::])
                self.text = f"Playing {song}"
                self.main.label.setText(self.text)
                self.main.label.repaint()
                self.speaker(self.text)

            elif self.text.startswith(("Search", "search")):
                ws.search_on_google(self.text[c + 1::])

            elif self.text in ("Tell me a joke", "tell me a joke"):
                self.text = pyjokes.get_joke("en","neutral")
                self.main.label.setText(self.text)
                self.main.label.repaint()
                self.speaker(self.text)

            elif self.text.startswith(("open","Open")):
                a = self.text[c + 1::]
                oa.open_application(self.text[c + 1::])
                self.text = f"Opening {a}"
                self.main.label.setText(self.text)
                self.main.label.repaint()
                self.speaker(self.text)

            elif self.text in ("What's the time","what's the time","time","tell me the time"):
                Time = datetime.datetime.now().strftime("%H:%M:%S")   
                self.text=f"Current time is {Time}"
                self.speaker(self.text)

            elif self.text in ("What's the date","what's the date","date","tell me the date","today's date"):
                date = datetime.date.today()  
                self.text=f"Today's date is {date}"
                self.speaker(self.text)

            elif self.text in ("Take a photo","take a photo","camera"):
                print("works")
                c=1
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    self.text="Unable to access the camera"
                ret, frame = cap.read()
                if not ret:
                    self.text="Failed to capture frame"
                cap.release()
                while True:
                    file_path = f"0{str(c)}.jpg"
                    if not os.path.exists(file_path):
                        cv2.imwrite(file_path, frame)
                        self.text=(f"Image captured and saved as '{file_path}'")
                        break
                    c+=1
            else:
                answer = ChatGpt.chat_gpt(self.text)
                self.text = answer
                self.main.label.setText(self.text)
                self.main.label.repaint()
                self.speaker(self.text)

        except sr.UnknownValueError:
            self.text = "Speech recognition could not understand audio"
            
        except sr.RequestError as e:
            self.text = "Could not request results from Google Speech Recognition service" + str(e)

    def check_os(self):
        system = platform.system()
        if system == "Windows":
            return "Windows"
        elif system == "Darwin":
            return "macOS"
        else:
            return "Unknown"

    def speaker(self, s):

        if self.check_os() == "Windows":
            # Initialize the TTS engine
            engine = pyttsx3.init()
            # Set the properties (optional)
            engine.setProperty("rate", 150)  # Speed of speech
            engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)
            engine.setProperty(
                'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
            engine.say(s)
            engine.runAndWait()

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
    sys.exit(app.exec())
