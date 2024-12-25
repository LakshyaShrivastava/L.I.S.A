import requests
import json
import os
import eel


from engine.speak import greet
from engine.features import playStartsSound

# API endpoint
url = "http://localhost:11434/api/chat"

if __name__ == "__main__":
    eel.init("webUI")

    playStartsSound()
    
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)



    # greet()
    # while True:
    #     question = str(input("Question: "))
    #     data = {
    #         "model" : "llama3.2:1b",
    #         "messages": [{"role":"user", "content":question}],
    #         "stream" : False
    #     }
    #     response = requests.post(url, json=data)
    #     response_json = json.loads(response.text)
    #     ai_reply = response_json["message"]["content"]
    #     print(ai_reply)
