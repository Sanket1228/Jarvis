import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning Sir")
        print("Good Morning Sir...")  
    elif hour <= 12 and hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon...")
    else:
        speak("Good Evening")
        print("Good Evening...")

    speak("I am Jarvis , How can I help you")
    print("I am Jarvis , How can I help you ? ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio,language='en-in')
            print("User Said : \n",query)
        except Exception as e:
            print("Can't Recognize, Say that again")
            return "None"

    return query


if __name__ == '__main__':
    wishme()
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching on wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\sanket\SoNg\Bollywood rock"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(1,100)]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        

