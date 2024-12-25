import pyttsx3
import speech_recognition as sr
from speech_recognition import Microphone
import eel

def greet():
    greeting = "Hi, I am Lisa. How may I help you?"
    speak(greeting)

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)

    engine.say(audio)
    engine.runAndWait()

@eel.expose
def take_commands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio)
        eel.DisplayMessage(f'User said: {query}')
        print(f'User said: {query}')
        speak(query)
        eel.ShowBlob()
    except Exception as e:
        print("Sorry I didnt get that.")
        return ""

    return query.lower()

if __name__ == "__main__":
    text = take_commands()
    speak(text)
