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
            Layanan = mendengar.recognize_google(suara, language='id-ID')
            print(Layanan)
        except:
            pass 
        return Layanan
    
def talk(audio):
    engine.say(audio)
    engine.runAndWait
    

def run_michelle():
    Layanan = perintah()    
    print(Layanan)
    if 'Open' in Layanan:
        video = Layanan.replace('Open','')
        pyt.speak('opening ' + video)
        print(video + 'opening..')
        pywhatkit.playonyt(video)

    if 'find' in Layanan:
        wiki = Layanan.replace('find','')
        hasil = wikipedia.summary(wiki, sentences=4)
        print(hasil)
        pyt.speak(hasil)


run_michelle()
