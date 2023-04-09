import speech_recognition as srec
import pyttsx3 as pyt
import pywhatkit
import wikipedia
import os
import re
import webbrowser
import datetime

engine =pyt.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >=0 and currentH <12:
        pyt.speak("Good Morning Bhatito")
    if currentH >=12 and currentH <18:
        pyt.speak("Good Afternoon Bhatito")
    if currentH >=18 and currentH <0:
        pyt.speak("Good night Bhatito")

greetMe()

def perintah():
    mendengar = srec.Recognizer() 
    with srec.Microphone() as source: 
        pyt.speak('hi i am michalle, can i help you?')
        print('Listening...')
        mendengar.pause_threshold = 0.9
        suara = mendengar.listen(source)
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
    if 'YouTube' in dengar:
        video = dengar.replace('YouTube','')
        pyt.speak('opening youtube ' + video)
        print(video + 'opening..')
        pywhatkit.playonyt(video)

    if 'Wikipedia' in dengar:
        wiki = dengar.replace('Wikipedia','')
        hasil = wikipedia.summary(wiki, sentences=4)
        print(hasil)
        pyt.speak(hasil)

    if 'Google' in dengar:
        reg_ex = re.search('where (.*)', dengar)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    if 'Open my github' in dengar:
        reg_ex = re.search('web (.*)', dengar)
        url = 'https://github.com/bhatito'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    
    if 'thanks' in dengar:
        pyt.speak('Thanks Mr.Bhatito have a nice day ')
        exit()
    else:
        pyt.speak('Can You Repeat Againt ?')

run_michelle()
