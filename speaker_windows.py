import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the properties (optional)
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def speak(text):
    engine.say(text)
    engine.runAndWait()

