import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer, QThread
from PyQt5.QtGui import QColor, QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedLayout,QGraphicsDropShadowEffect
import socket
import speech_recognition as sr
import pyttsx3
import platform
from gtts import gTTS
import threading
from threading import Thread
import os
import jokes
import datetime
import cv2
import time
import random
import DATABASE
from main_window import Ui_MainWindow
from splash_ui import Ui_SplashScreen
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
        self.timer.start(20)  # timeout for 20 milliseconds
        QtCore.QTimer.singleShot(0, lambda: self.splash.label_2.setText("Shubham"))
        QtCore.QTimer.singleShot(4000, lambda: self.splash.label_2.setText("Bhavya"))#changes text after given time
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
                self.main.main.listening_button.setEnabled(False)
                self.main.text = "No internet connection"
        counter += 1
class ListeningThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.speech_rec()

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

        self.main.main_close.pressed.connect(self.closewindow)
        self.main.listening_button.pressed.connect(self.listening)
        self.main.help_button.pressed.connect(self.help)
        self.main.help_close.pressed.connect(self.close_commands)

        self.l=["Hello, how may I be of service?","Hi! What can I do for you?","Hey, how can I help?","Hi there! Ready to get started?","Ahoy, captain! What's on your mind today?","What can I help you with today?"]
        self.text=random.choice(self.l)

        layout=QStackedLayout()
        layout.addWidget(self.main.help_close)
        layout.addWidget(self.main.speaker_label)
        layout.addWidget(self.main.mic_label)
        layout.addWidget(self.main.gif_label)
        layout.addWidget(self.main.listening_button)
        layout.addWidget(self.main.main_close)
        layout.addWidget(self.main.help_button)
        layout.setCurrentIndex(4)
        self.setLayout(layout)
        #self.main.anim.stop()
        self.main.gif_label.show()
        self.main.main_close.show()
        self.main.help_button.show()

    def gif_start(self):
        self.main.anim.start()

    def close_commands(self):
        self.main.scrollArea.setGeometry(40, 0, 695, 190)
        self.main.help_close.hide()
        self.main.gif_label.show()
        self.main.listening_button.show()
        self.text=random.choice(self.l)
        
        
    def listening(self):
        self.main.gif_label.hide()
        self.main.mic_label.show()
        self.text = "Listening..."
        self.thread = ListeningThread(self)
        self.thread.finished.connect(self.thread_finished)
        self.thread.start()

    def thread_finished(self):
        self.main.mic_label.hide()
        self.main.speaker_label.hide()
        self.main.gif_label.show()
        self.main.listening_button.show()
        self.main.scrollArea.setGeometry(40, 0, 695, 135)

    def help(self):#help button
        self.main.help_close.show()
        self.main.gif_label.hide()
        self.main.listening_button.hide()
        self.main.scrollArea.setGeometry(40, 0, 695, 220)
        self.text= """COMMANDS
        Maps: Direction to <destination>
        Weather: What's the weather in <location> or What's the weather
        Music: Play <song_name>
        Google: Search <your_query>
        Joke: Tell me a joke 
        Time: Whats the time
        Date: Whats the date
        Open apps:Open <app_name>
        Click a Photo: Take my photo
        ChatGpt: <your_query>"""
        self.main.main_label.setText(self.text)

    def closewindow(self):#close button
        exit()

    def speech_rec(self):
        self.gif_start()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = r.listen(source,timeout=10)
                self.main.mic_label.hide()
                self.main.gif_label.hide()
                self.main.listening_button.hide()

            except sr.WaitTimeoutError:
                self.error()
                return None
        audio_rec = r.recognize_google(audio).capitalize()
        self.text =f"You said: {audio_rec}"
        time.sleep(2)
        try:
            DATABASE.save_prompt(audio_rec)
            b = audio_rec.split()

            if audio_rec.startswith(("direction to","Direction to","directions to","Directions to")):
                l_2=["Mapping out the details...","Exploring the territories...","Navigating the data...","Calculating the coordinates..."]
                self.text=random.choice(l_2)
                time.sleep(2)
                maps.open_maps(audio_rec[12::].strip())

            elif audio_rec.startswith(("What's the temperature in","Temperature in","What's the weather in")):
                a=b.index("in")
                l_2=["Checking the skies...","Consulting the weather gods...","Calibrating the weather radar...","Looking out your window..."]
                self.text=random.choice(l_2)
                time.sleep(2)
                place = ' '.join(b[a+1:]).strip()
                weather = get_temp.get_current_temperature_place(place)[0]
                temperature = get_temp.get_current_temperature_place(place)[1]
                self.text = f"The current Weather in {place.capitalize()} is {weather.capitalize()} and the Temperature is {temperature} Celsius."
                self.main.main_label.setText(self.text)
                self.speaker(self.text)

            elif audio_rec.startswith(("What's the weather","Temperature","What's the temperature")):
                l_2=["Checking the skies...","Consulting the weather gods...","Calibrating the weather radar...","Looking out your window..."]
                self.text=random.choice(l_2)
                time.sleep(2)
                weather=get_temp.get_current_temperature()[0]
                temperature=get_temp.get_current_temperature()[1]
                place=get_temp.get_current_temperature()[2].capitalize()
                self.text=f"The current Weather in {place} is {weather.capitalize()} and temperature is {temperature} Celsius."
                self.main.main_label.setText(self.text)
                self.speaker(self.text)

            elif audio_rec.startswith(("Play")) and self.check_os() == "Windows":
                l_2=["Music vibes loading, enjoy the melody...","Warming up the speakers, hold on...","Setting the stage for your song..."]
                self.text=random.choice(l_2)
                time.sleep(2)
                sw.music_play(audio_rec[5::].strip())
                self.text = f"Playing {audio_rec[5::]}"
                self.main.main_label.setText(self.text)

            elif audio_rec.startswith(("Play")) and self.check_os() == "macOS":
                l_2=["Music vibes loading, enjoy the melody...","Warming up the speakers, hold on...","Setting the stage for your song..."]
                self.text=random.choice(l_2)
                time.sleep(2)
                sm.play_song(audio_rec[5::].strip())
                self.text = f"Playing {audio_rec[5::]}"
                self.main.main_label.setText(self.text)

            elif audio_rec.startswith(("Search")):
                ws.search_on_google(audio_rec[7::].strip())

            elif audio_rec in ("Tell me a joke"):
                self.text = jokes.joke()
                self.main.main_label.setText(self.text)
                self.speaker(self.text)

            elif audio_rec.startswith(("Open")):
                a = audio_rec[5::]
                self.text="Firing up the app's engines..."
                time.sleep(2)
                oa.open_application(audio_rec[5::])
                self.text = f"Opening {a.capitalize()}"
                self.main.main_label.setText(self.text)
                self.speaker(self.text)

            elif audio_rec in ("What's the time","Tell me the time","What is the time","What's the time right now","What is the time right now"):
                l_2=["Checking the hourglass of time...","Checking the calendar and the stars...","Clocks are ticking, just a moment...","Time-traveling through data streams...","Syncing with the cosmic clock..."]
                self.text=random.choice(l_2)
                time.sleep(2)
                Time = datetime.datetime.now().strftime("%H:%M:%S")   
                self.text=f"Current time is {Time}"
                self.speaker(self.text)

            elif audio_rec in ("What's the date","Tell me the date","Today's date","What is the date","What's today's day","What is today's day"):
                l_2=["Checking the hourglass of time...","Checking the calendar and the stars...","Clocks are ticking, just a moment...","Time-traveling through data streams...","Syncing with the cosmic clock..."]
                self.text=random.choice(l_2)
                time.sleep(2)
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
                self.text="Say Cheese..."
                time.sleep(1)
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
                self.main.main_label.setText(self.text)
                self.speaker(self.text)
                
            
        except sr.UnknownValueError:
            self.error
            print("works")
            
        except sr.RequestError as e:
            self.text = "Could not request results from Google Speech Recognition service" + str(e)
        self.repeat()
    def repeat(self):
        self.main.scrollArea.setGeometry(40, 0, 695, 135)
        self.main.speaker_label.hide()
        self.main.mic_label.hide()
        self.main.gif_label.show()
        self.main.listening_button.show()

    def error(self):
        self.text="Try Again!"
        self.main.mic_label.hide()
        self.main.gif_label.show()
        self.main.listening_button.show()
    def display(self):
        self.main.main_label.setText(self.text)
        self.main.main_label.repaint()

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
            tts = gTTS(s, lang='en')
            temp_file = "temp.mp3"
            tts.save(temp_file)
            os.system(f"afplay {temp_file}")
            os.remove(temp_file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())