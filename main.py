import speech_recognition as sr
import os
import webbrowser
import datetime
import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice")  # Only For Windows User
import openai
from config import apikey
import datetime
import random
import numpy as np


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Basha: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    speaker.speak(text) # For Mac Just give os.system(f"say {text}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language= "en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured Boss Sorry from Baaasha"
        
if __name__ =='__main__':
    say("Hey I am Baaasha A i ")
    while True:
        print("Listening...")
        query = takecommand()
        sites = [["youtube","https://Youtube.com"], ["movie","https://1tamilmv.legal"], ["github","https://github.com"], ["chat","https://chatgpt.com/"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} boss")
                webbrowser.open(site[1])
        if "the time".lower() in query.lower():
            hr = strfTime = datetime.datetime.now().strftime("%H")
            min = strfTime = datetime.datetime.now().strftime("%M")
            sec = strfTime = datetime.datetime.now().strftime("%S")
            say(f"Boss the time is {hr} {min}")

        elif "open spotify".lower() in query.lower():
            path = os.system("where spotify")
            os.system("start C:/Users/harim/AppData/Local/Microsoft/WindowsApps/Spotify.exe")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query) # This Function is only for Open AI

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        # say(query)