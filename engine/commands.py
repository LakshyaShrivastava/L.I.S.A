import speech_recognition as sr
import eel
import os
import time
import requests
import json

from engine.constants import ASSISTANT_NAME, API_ENDPOINT
from engine.speak import speak

@eel.expose
def take_command():
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
        # speak(query)
    except Exception as e:
        print("Sorry I didnt get that.")
        return ""

    return query.lower()

@eel.expose
def parse_all_commands():
    query = take_command()
    print(query)
    if "open" in query:
        handle_open(query)
    else:
        query_llama(query)

def handle_open(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower() # not necesary i think

    if query != "":
        speak("Opening" + query)
        os.system('start' + query) # using command prompt start command to open apps
    else:
        speak("Not found")

    eel.ShowBlob()  

def query_llama(query):
    query = query.replace(ASSISTANT_NAME, "")
    query.lower()

    data = {
            "model" : "llama3.2:1b",
            "messages": [{"role":"user", "content":query}],
            "stream" : False
    }
    response = requests.post(API_ENDPOINT, json=data)
    response_json = json.loads(response.text)
    ai_reply = response_json["message"]["content"]
    speak(ai_reply)
    # print(ai_reply)
    eel.ShowBlob() 
