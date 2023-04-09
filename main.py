import speech_recognition as srec
import pyttsx3 as pyt
import pywhatkit
import wikipedia
import os
import re
import webbrowser

engine =pyt.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def perintah():
    mendengar = srec.Recognizer() 
    with srec.Microphone() as source: 
        pyt.speak('hi i am michalle, can i help you?')
        print('Listening...')
        mendengar.pause_threshold = 0.9
        suara = mendengar.listen(source, phrase_time_limit=5)
        try:
            print('Processing...')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except:
            pass 
        return dengar
    
def talk(audio):
    engine.say(audio)
    engine.runAndWait
    

def run_michelle():
    dengar = perintah()    
    print(dengar)
    if 'Open' in dengar:
        video = dengar.replace('Open','')
        pyt.speak('opening ' + video)
        print(video + 'opening..')
        pywhatkit.playonyt(video)

    if 'find' in dengar:
        wiki = dengar.replace('find','')
        hasil = wikipedia.summary(wiki, sentences=4)
        print(hasil)
        pyt.speak(hasil)
    

run_michelle()
