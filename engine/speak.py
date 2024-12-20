import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def greet():
    greeting = "Hi, I am your desktop assistant. How may I help you?"
    speak(greeting)
    print(greeting)
    