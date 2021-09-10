import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")
    speak("I am elli, Mam. Please tell me how may i help you")     

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
       # print(e)
        print("say that again please...")
        return "None"   
    return query

def sendEmail(to, content):  
    server = smtplib.SMTP('smtp.gmail.com',587 ) 
    server.ehlo()
    server.starttls()
    server.login('yashika13v@gmail.com','')
    server.sendmail('yashikav13@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
   #while True:
   if 1:
    query = takecommand().lower()
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")
          
    elif 'play music' in query:
       music_dir = 'D:\\python\\songs'
       song = os.listdir(music_dir)
       print(song)
       os.startfile(os.path.join(music_dir,song[1]))
       
    elif 'the time' in query:
       strTime = datetime.datetime.now().strftime("%H:%M:%S")
       speak(f"sir the time is {strTime}")

    elif 'open code' in query:
        cpath = "C:\\Users\\Yashika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(cpath)

    elif 'send email' in query:
        try:
            speak("what should I say?")
            content = takecommand()
            to = "19egjcs858@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("not able to send this email")
