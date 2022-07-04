
import pyjokes
import requests
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine. setProperty("rate", 178)


  

My_joke = pyjokes.get_joke(language="en", category="neutral")
  
speak(My_joke)