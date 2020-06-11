import pyttsx3 #pip install pyttsx3 in shell
import speech_recognition as sr #pip install speechRecognition in shell
import datetime
import wikipedia #pip install wikipedia in shell
import webbrowser
import os
import sys
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon!")   

    else:
        speak("Good Evening")  
        print("Good Evening!")  

    speak("I am smith your voice assistant, Sir Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing")   
        query = r.recognize_google(audio, language='en-in')
        print('you said : '+query)

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        speak("Say that again please....") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mymail@gmail.com', 'mypassword')
    server.sendmail('mymail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open w3 school' in query:
            webbrowser.open("https://w3schools.com")   
        elif 'open facebook' in query:
            webbrowser.open("https://facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")
        elif 'open linked in' in query:
            webbrowser.open("https://linkedin.com")
        elif 'open driems website' in query:
            webbrowser.open("https://driems.ac.in")
        elif 'open bput website' in query:
            webbrowser.open("https://bput.ac.in")
        elif 'hello' in query:
            speak('Hello Sir')
        elif "what's up" and 'whatsapp'and 'how are you' in query:
            stMsgs = ['Just doing my things!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'bye smith' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'play music' in query:
            music_dir='E:\\all audio'
            music=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,music[random.randrange(0,50)]))
            speak('Okay, here is your music! Enjoy!')
        elif 'play video' and 'play movie' in query:
            video_dir = 'E:\\all video\\Movie\\bollywood'
            videos = os.listdir(video_dir)    
            os.startfile(os.path.join(video_dir, videos[random.randint(0,50)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'email to santosh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    
