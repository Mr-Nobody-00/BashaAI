import speech_recognition as sr
import os
import webbrowser
import datetime
import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice")  # Only For Windows User
import datetime
import random
import numpy as np


chatStr = ""

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
        print(query)
        sites = [["youtube","https://Youtube.com"], ["movie","https://1tamilmv.bike"], ["github","https://github.com"], ["chat","https://chatgpt.com/"], ]
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

        elif "Quit".lower() in query.lower():
            exit()

        # say(query)