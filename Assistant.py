import webbrowser
import speech_recognition
import os
import datetime
import time
import pyttsx3
import wikipedia
import smtplib
import requests
import json
import sys
from selenium import webdriver
import bs4
import re
import lxml
import json
import schedule

engine1=pyttsx3.init('sapi5')
voice=engine1.getProperty('voices')
engine1.setProperty('voice',voice[0].id)
firstname='Bharat'
lastname='saini'
fullname='Bharat saini'
email='yourmain@email.com'
sched=[]
price_rem={}
links_rem={}
def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12 :
        speak('hey sir! Good morning')
    elif hour>=12 and hour<=17:
        speak('Hello sir ! Good noon..')
    elif hour>=17 and hour<=20:
        speak('hey sir! Good evening')
    elif hour>=21 and hour<=24:
        speak('hello sir! How was your day?')

def orders(): 
    listen_me=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening....')
        listen_me.pause_threshold=1
        audio=listen_me.listen(source)
    try:
        command = listen_me.recognize_google(audio,language='en-in')
        print('Recognizing')
        return command
    except Exception as e:
        print('Could not get you',e)
   

def check_amazon():
    with open('assistant.json','r') as file:
        file.read(json.loads(price_rem))
        file.read(json.loads(links_rem))
    if price_rem['Amazon']!=0:
        headers={'user-agent':'your usernheaders'}
        webbrowser.open(links_rem['Amazon'])
        req = requests.get(url,headers=headers)
        soup=bs4.BeautifulSoup(req.text , 'lxml')
        prices=str(soup.find(class_='a-price-whole').get_text())
        time.sleep(20)
        if price_rem['Amazon'] < prices:
            speak('Sir price has been reduced , click the link below to visit the site!')
            links_rem['Amazon'].replace(' ','+')
            print(links_rem['Amazon'])
    elif price_rem['Flipkart']!=0:
        headers={'user-agent':'your user headers'}
        webbrowser.open(links_rem['Flipkart'])
        req = requests.get(links_rem['Flipkart'],headers=headers)
        soup=bs4.BeautifulSoup(req.text , 'lxml')
        prices=str(soup.find(class_='_1vC4OE _2rQ-NK').get_text())
        time.sleep(20)
        if price_rem['Flipkart'] < prices:
            speak('Sir price has been reduced , click the link below to visit the site!')
            links_rem['Flipkart'].replace(' ','+')
            print(links_rem['Flipkart'])



def speak(audio):
    engine1.say(audio)
    engine1.runAndWait()
# def speak(audioString):
#     print(audioString)
#     tts = gTTS(text=audioString, lang='en')
#     os.system(".mp3")
    while True:
        command=orders().lower()
        if ('what is' or 'who is' or 'what are' or 'who are')  in command:
            speak("Here's what i found!")
            info = wikipedia.summary(command, sentences=3)
            speak('According to wikipedia')
            speak(info)
        elif ('open' and  'youtube') in command:
            try:
               webbrowser.open('https://www.youtube.com')
               speak('I have opened')
            except Exception:
                print('Sorry')
        elif ('open' and  'instagram') in command:
            try:
                webbrowser.open('https://www.instagram.com')
                speak('I have opened')
            except Exception:
                print('Sorry sir')
        elif ('open' and 'facebook') in command:
            try:
                webbrowser.open('https://www.facebook.com')
                speak('Here"s your facebook')
            except Exception:
                print('Sorry sir! My bad')
        elif ('open' and  'stackoverflow') in command:
            try:
                webbrowser.open('https://www.stackoverflow.com')
                speak('Here it is Sir!')
            except Exception:
                print('Sorry sir! My bad')
        elif ('open' and 'chrome') in command:
            try:
                webbrowser.open('https://www.google.com/')
                speak('i have opened')
            except Exception:
                print('Sorry sir! My Bad')
        elif ('read news') in command:
            try:
                link='https://newsapi.org/v2/top-headlines?country=in&apiKey=yourapikey'
                response=requests.get(link)
                text=response.text
                json_con=json.loads(text)
                for i in range(0,9):
                    speak(json_con['articles'][i]['title'])
            except Exception:
                speak('Sorry sir')
        elif ("todays" and "weather") in command:
            try:
                link2='http://api.apixu.com/v1/current.json?key=yourapikey'
                response=requests.get(link)
                text2=response.text
                json_tem=json.loads(text2)
                speak(json_tem['temp_c'])
            except Exception:
                speak(' I am Sorry sir')
        elif ('login' and 'to' and  'facebook') in command:
                    try:
                        listen_me=speech_recognition.Recognizer()
                        speak('What is your  username sir!')
                        with speech_recognition.Microphone() as source3:
                             print('Listening to you...')
                             listen_me.pause_threshold=1
                             audio=listen_me.listen(source3)
                             username = listen_me.recognize_google(audio,language='en-in')
                             print('Recognizing')
                    except Exception as e:
                         print('Could not get you',e)
                    try:
                        speak('What is your password sir!!')
                        with speech_recognition.Microphone() as source2:
                                print('Listening to you...')
                                listen_me.pause_threshold=1
                                audio=listen_me.listen(source2)
                                password=listen_me.recognize_google(audio,language='en-in')
                                print('Recognizing')
                                print(password)
                                password=password.replace(' ','')
                    except Exception as e:
                        print('could not get you',e)
                    try:
                        driver=webdriver.Chrome('path to the chrome driver\\chromedriver.exe')
                        driver.get('https://www.facebook.com/') 
                        print("Opened facebook") 
                        time.sleep(5) 
                        username_box = driver.find_element_by_id('email') 
                        username_box.send_keys(username) 
                        time.sleep(4)
                        password_box = driver.find_element_by_id('pass') 
                        password_box.send_keys(password)  
                        driver.find_element_by_id('loginbutton').click() 
                        speak('I have opened sir!')
                    except Exception:
                        speak('Sorry sir!')
        elif ('create' and  'my' and 'instagram' and 'account') in command:
                    try:
                        speak('Are you making this  account for yourself sir?')
                        with speech_recognition.Microphone() as source5:
                                listen_me=speech_recognition.Recognizer()
                                listen_me.pause_threshold=1
                                audio=listen_me.listen(source5)
                                input1=listen_me.recognize_google(audio,language='en-in')
                        if 'yes Jarvis' or 'ofcourse' in input1:
                                    speak('What would be your username sir?')
                                    with speech_recognition.Microphone() as source8:
                                         listen_me=speech_recognition.Recognizer()
                                         listen_me.pause_threshold=1
                                         audio=listen_me.listen(source8)
                                         username=listen_me.recognize_google(audio,language='en-in')
                                         print('Recognizing!')
                                         username=username.replace(' ','')
                                         speak("Assign a password for security sir? ")
                                         listen_me.pause_threshold=1
                                         audio=listen_me.listen(source8)
                                         password=listen_me.recognize_google(audio,language='en-in')
                                         print('Recognizing!')
                                         password=password.replace(' ','')
                                        
                        else:
                                    speak('What would be the name sir?')
                                    with speech_recognition.Microphone() as source4: 
                                        listen_me=speech_recognition.Recognizer()
                                        listen_me.pause_threshold=1
                                        audio=listen_me.listen(source4)
                                        firstname=listen_me.recognize_google(audio,language='en-in')
                                        lastname=listen_me.recognize_google(audio,language='en-in')
                                        firstname=firstname.replace(' ','')
                                        lastname=lastname.replace(' ','')
                                        fullname=(str(firstname+lastname).split(' '))
                                    speak('tell me your email or phone nunmber')
                                    with speech_recognition.Microphone() as source6:
                                        listen_me=speech_recognition.Recognizer()
                                        listen_me.pause_threshold=1
                                        audio=listen_me.listen(source6)
                                        email=listen_me.recognize_google(audio,language='en-in')
                                        email=email.replace(' ','')
                                    speak('what would be your username?')
                                    with speech_recognition.Microphone() as source7:
                                        listen_me=speech_recognition.Recognizer()
                                        listen_me.pause_threshold=1
                                        audio=listen_me.listen(source7)
                                        username=listen_me.recognize_google(audio,language='en-in')
                                        username=email.replace(' ','')
                                    speak('Tell me your password sir!')
                                    with speech_recognition.Microphone() as source9:
                                        speak("Assign a password for security sir? ")
                                        listen_me=speech_recognition.Recognizer()
                                        listen_me.pause_threshold=1
                                        audio=listen_me.listen(source9)
                                        password=listen_me.recognize_google(audio,language='en-in')
                                        print('Recognizing!')
                                        password=password.replace(' ','')
                        try:
                            driver=webdriver.Chrome('C:\\Users\\VISHAL SAINI\\Desktop\\python\\Jarvis\\chromedriver.exe')
                            driver.get('https://www.instagram.com/')  
                            time.sleep(5) 
                            email_box= driver.find_element_by_name('emailOrPhone') 
                            time.sleep(5) 
                            fullname_box = driver.find_element_by_name('fullName') 
                            time.sleep(4)
                            username_box = driver.find_element_by_name('username') 
                            time.sleep(3)
                            password_box=driver.find_element_by_name('password')  
                            time.sleep(3)
                            email_box.send_keys(email)
                            time.sleep(2)
                            fullname_box.send_keys(fullname)
                            time.sleep(3)
                            username_box.send_keys(username)
                            time.sleep(2)
                            password_box.send_keys(password).send_keys('keys.ENTER')
                            time.sleep(2)
                            speak('Welcome to Instagram World sir!')
                        except Exception:
                            speak('I think username is already taken')    
                    except Exception:
                        speak('Sorry sir!')                   
        elif ('play'and 'youtube' and 'video') in command:
            speak('which video would you like to play?')
            with speech_recognition.Microphone() as source10:
                            listen_me=speech_recognition.Recognizer()
                            listen_me.pause_threshold=1
                            audio=listen_me.listen(source10)
                            yt_video=listen_me.recognize_google(audio,language='en-in')
            url='https://www.youtube.com/results?search_query='+yt_video
            req=requests.get(url)
            soup=bs4.BeautifulSoup(req.text,'lxml')
            linktag=soup.select_one('a[href^="/watch"]')
            webbrowser.open('https://www.youtube.com'+linktag.get('href')) 
        elif ('online shopping' or 'shopping' or 'e-shopping') in command:
            speak('What do you want to buy, sir?')
            with speech_recognition.Microphone() as source11:
                        listen_me=speech_recognition.Recognizer()
                        listen_me.pause_threshold=1
                        audio=listen_me.listen(source11)
                        product=listen_me.recognize_google(audio,language='en-in')
            speak('From where would you like to buy? Amazon or Flipkart')
            with speech_recognition.Microphone() as source12:
                      listen_me=speech_recognition.Recognizer()
                      listen_me.pause_threshold=1
                      audio=listen_me.listen(source12)
                      site=listen_me.recognize_google(audio,language='en-in')
            if 'Amazon' in site:
                amazon_prod=product
                headers={'user-agent':'your user agent'}
                amazon_url=('https://www.amazon.com/s?k='+amazon_prod)
                webbrowser.open(amazon_url)
                print('GO shop')
                time.sleep(60)
                print('listening..')
                with speech_recognition.Microphone() as source13:
                    listen_me=speech_recognition.Recognizer()
                    listen_me.pause_threshold=1
                    audio=listen_me.listen(source13)
                    input10=listen_me.recognize_google(audio, language='en-in')
                if 'set reminder' in input10:
                    speak('set the price sir!')
                    with speech_recognition.Microphone() as source14:
                        listen_me=speech_recognition.Recognizer()
                        listen_me.pause_threshold=1
                        audio=listen_me.listen(source14)
                        amazon_rem=listen_me.recognize_google(audio, language='en-in')
                    price_rem={'Amazon':amazon_rem}
                    links_rem={'Amazon':amazon_url}                  
                    with  open('assistant.json' , 'a') as file:
                        file.write(json.dumps(price_rem))
                        file.write(json.dumps(links_rem))
                    check_amazon()
            elif 'Flipkart' in site:
                flipkart_prod=product
                headers={'user-agent':'your user agent'}
                flipkart_url=('https://www.flipkart.com/search?q='+flipkart_prod)
                webbrowser.open(flipkart_url)
                print('Happy shopping')
                time.sleep(60)
                print('Listening..')
                with speech_recognition.Microphone() as source13:
                    listen_me=speech_recognition.Recognizer()
                    listen_me.pause_threshold=1
                    audio=listen_me.listen(source13)
                    input10=listen_me.recognize_google(audio, language='en-in')
                    print(input10)
                if 'set reminder' in input10:
                    speak('set the price sir!')
                    with speech_recognition.Microphone() as source14:
                        listen_me=speech_recognition.Recognizer()
                        listen_me.pause_threshold=1
                        audio=listen_me.listen(source14)
                        flipkart_rem=listen_me.recognize_google(audio, language='en-in')
                    price_rem['Flipkart']=flipkart_rem
                    links_rem['Flipkart']=flipkart_url
                    speak('I will remind you sir!')
                    with open('assistant.json', 'a') as file:
                        file.write(json.dumps(price_rem['Flipkart']))
                        file.write(json.dumps(links_rem['Flipkart']))
        elif ('google' and 'search') in command:
                speak('What should i search?')
                with speech_recognition.Microphone() as source15:
                    listen_me=speech_recognition.Recognizer()
                    listen_me.pause_threshold=1
                    audio=listen_me.listen(source15)
                    input11=listen_me.recognize_google(audio, language='en-in')
                google_url=('https://www.google.com/search?source=hp&ei='+input11)
                speak('how manu suggestions should i give?')
                with speech_recognition.Microphone() as source16:
                    listen_me=speech_recognition.Recognizer()
                    listen_me.pause_threshold=1
                    audio=listen_me.listen(source16)
                    input12=int(listen_me.recognize_google(audio, language='en-in'))
                req=requests.get(google_url)
                soup=bs4.BeautifulSoup(req.text, 'lxml')
                links=soup.find('a',attr=['href '])
                webbrowser.open(links.get('href'))
        elif 'set my schedule' in command:
            speak('Tell me sir!')
            with speech_recognition.Microphone() as source17:
                    listen_me=speech_recognition.Recognizer()
                    listen_me.pause_threshold=1
                    audio=listen_me.listen(source17)
                    schedule1=(listen_me.recognize_google(audio, language='en-in'))
            sched.append(schedule1)
            with open('assistant.json','a') as file:
                file.write(json.dumps(sched))
        elif ('my' and 'schedule') in command:
            with open('assistant.json','r') as file:
                data=file.read(json.load(sched))3
            speak(data)
            
              
                



                
           
