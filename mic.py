def speech_rec():
    global text
    import speech_recognition as sr

    # Initialize the recognizer
    r = sr.Recognizer()

    # Open the microphone and listen for speech
    with sr.Microphone() as source:
        # print("Speak something...")
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError as e:
        print("Error:", str(e))
    return text
