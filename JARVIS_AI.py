import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver
import pyfirmata

board = pyfirmata.Arduino('COM3')

url = 'https://kvsmat.in/'

url1 = 'https://www.youtube.com/watch?v=bdqj0T6F5HU'

chrome_path = ' C:/Program Files/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back Abhinav ")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning Abhinav")

    elif hour>=12 and hour<18:
        speak("Good Afternoon abhinav")

    elif hour>=18 and hour<24:
        speak("Good Evening abhinav")

    else:
        speak("Good Night abhinav")

    speak("ultron AI at your Service. Please tell me how can I help You ")

    if hour>=6 and hour<12:
        speak("Lets start our day with  a proverb Time is money ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Abhinav Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Senderemail@gmail.com', 'Password')
    server.sendmail('Senderemail@gmail.com', to, content)
    server.close()


            

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
           
           

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' +text )
                wb.get(chrome_path).open(text)
            except Exception as e:
                print(e)

        elif 'your name' and 'who are you' in query:
             speak('I am  Ultron ai devloped by abhinav  and  x-d ')
         
        elif 'how is the weather' and 'weather' in query:
           
            exec(open('weather.py').read())
        
        elif 'search kvs mat in chrome'  in query:
          
            speak("searching")
            wb.get(chrome_path).open(url)

        elif 'how are you' in query:    
            speak('i am fine how about you')
        
        elif 'fine' in query:
            speak('Okay thats nice')
        
        elif 'sing birthday song' in query:

             wb.get(chrome_path).open(url1)

        elif 'what can you do' in query:
            speak ('open websites Example open youtube     time Example what time it is date Example what date it is launch applications Example launch chrometell me Example tell me about India weather Example what weather/temperature in virudhunagar ')
                       

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'hello' in query:  
            speak(f"hi, sir this abhinavAI here")
            
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'email to harry' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ReciversEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")      

        elif 'open code' in query:
            codePath = "C:\\Users\\user account\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\Program Files\Google\chrome\Application\chrome.exe "#ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)     


        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        
        elif 'turn on the light' in query:
            speak("OK,sir turning on the Lights")
            while True:
                   board.digital[13].write(1)
            speak("Lights are on")
            sleep.
        
        elif 'turn off light' in query:
            speak("OK,sir turning off the Lights")
            while True:
                board.digital[13].write(0) 
            speak("Lights are off")



        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()
        
        elif 'today news' and 'news' in query:
            exec(open('news.py').read())
        
        