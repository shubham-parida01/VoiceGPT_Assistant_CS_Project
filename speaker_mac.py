from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
def speak():
    f = open("Output.txt","r")
    text = f.readline()
    tts = gTTS(text, lang='en')

    temp_file = "temp.mp3"
    tts.save(temp_file)

    audio = AudioSegment.from_file(temp_file, format="mp3")

    play(audio)

    os.remove(temp_file)


