import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak("Hey, I'm Desker, What Can I Do For You?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en=in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Can't Hear you.")
        print("Please Say that again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Your Password')
    server.sendmail('Your Email', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # if 1: #For only one command.
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'play music' in query:
            music_dir = 'E:\\sd\\My Music\\English'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'code' in query:
            codePath = 'C:\\Users\\Avi\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                content = takeCommand()
                to = "receiver@email.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I Can't send this email")

        elif 'quit' in query:
            exit()
