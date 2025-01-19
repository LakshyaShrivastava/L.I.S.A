import pyttsx3
import eel
import time

def greet():
    greeting = "Hi, I am Lisa. How may I help you?"
    speak(greeting)

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    eel.DisplayMessage(audio)
    engine.say(audio)
    engine.runAndWait()
    