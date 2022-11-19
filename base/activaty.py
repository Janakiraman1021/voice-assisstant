import datetime
import smtplib
from .general import speak
import wikipedia
import speech_recognition as sr #pip install speechRecognition
import webbrowser
# import pyautogui as pg

def time_now():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

def play_song():
    speak("Which Song I Should Play")
    #music_dir = ""
    #songs = os.listdir(music_dir)
    #speak('Playing Your Songs ')
    #os.startfile(os.path.join(music_dir, songs[0]))
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    print("recognising song name")
    song = r.recognize_google(audio, language='en-in')
    webbrowser.open("https://music.youtube.com/watch?v=%s"%song)


def wiki(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", " ")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Your Personal Voice Assistant JanakiRaman. Please tell me how may I help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('janakiramankv1021@gmail.com', '')
    server.sendmail('janakiramankv1021@gmail.com',to, content)
    server.close()

def send_mail():
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "janakiramankeerthivelan21@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry . I am not able to send this email")
        
