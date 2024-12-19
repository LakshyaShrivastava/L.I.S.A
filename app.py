import requests
import json

from speak import greet

# API endpoint
url = "http://localhost:11434/api/chat"

if __name__ == "__main__":
    greet()
    while True:
        question = str(input("Question: "))
        data = {
            "model" : "llama3.2:1b",
            "messages": [{"role":"user", "content":question}],
            "stream" : False
        }
        response = requests.post(url, json=data)
        response_json = json.loads(response.text)
        ai_reply = response_json["message"]["content"]
        print(ai_reply)
