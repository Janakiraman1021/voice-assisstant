#custom package

from base.general import speak, takeCommand
from base.activaty import ( wishMe,sendEmail, wiki, 
                           play_song, time_now, send_mail )

#pip packages

import time as t
import os
import wikipedia #pip install wikipedia
import webbrowser
import speech_recognition as sr
import datetime


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            wiki(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music from youtube' in query:
            play_song()
            
        elif 'the time' in query:
            time_now()

        elif 'open code' in query:
            codePath = "D:\\voice assisstant\\voice.py"
            os.startfile(codePath)

        elif 'send email' in query:
            send_mail()