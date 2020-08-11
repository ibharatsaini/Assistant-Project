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
import cv2
import numpy as np1
from os import listdir
from os.path import isfile, join
import pyautogui
import subprocess
# from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import webbrowser
import base64
import email
from email.mime.text import MIMEText


a='1'
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
firstname='first name'
lastname='last name'
fullname='full name'
email='email id '
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
    # elif hour>=19 and hour<=89:
    #     spea("Not valid!"

def orders(): 
    listen_me=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:        
        print('Listening!!!')
        listen_me.pause_threshold=1
        listen_me.adjust_for_ambient_noise(source,duration=1)
        audio=listen_me.listen(source)
    try:
        command = listen_me.recognize_google(audio,language='en-in')
        print('Recognizing!')
        return command
    except Exception as e:
        print('Could not get you',e)
def check_amazon():
    with open('your json file"s path where all the products to track are listed,'r') as file:
        file.read(json.loads(price_rem))
        file.read(json.loads(links_rem))
    if price_rem['Amazon']!=0:
        headers={'Browser headers here'}
        webbrowser.open(links_rem['Amazon'])
        req = requests.get(links_rem['Amazon'],headers=headers)
        soup=bs4.BeautifulSoup(req.text , 'lxml')
        prices=str(soup.find(class_='a-price-whole').get_text())
        time.sleep(20)
        if price_rem['Amazon'] < prices:
            speak('Sir price has been reduced , click the link below to visit the site!')
            links_rem['Amazon'].replace(' ','+')
            print(links_rem['Amazon'])
    elif price_rem['Flipkart']!=0:
        headers={'Browser headers here'}
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
    engine.say(audio)
    engine.runAndWait()


face_classifier=cv2.CascadeClassifier('Your xml file path')
    
data_path='Your jpeg files path'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]
Training_Data, Labels = [], []
    
for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        if '.jpg' in image_path:
            images=(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE))
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)
Labels = np.asarray(Labels, dtype=np.int32)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data), np.asarray(Labels))
print('trained')
    
loop=True
loop2=True
loop3=True
while loop==True:
    def face_detector(img):
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.1,10)
        if faces is():
                return img,[]
        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                roi=img[y:y+h,x:x+w]
                roi=cv2.resize(roi,(200,200))
        return img,roi
    cap=cv2.VideoCapture(0)
    while loop2==True:
        ret,frame=cap.read()
        image,face=face_detector(frame)
        try:
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                result=model.predict(face)
                if result[1] < 500:
                        confidence=int(100*(1-(result[1]/300)))
                        percent=str(confidence)+'%user'
                if confidence > 80:
                        cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 222), 2)
                        cv2.imshow('Face Cropper', image)
                        loop2=False
                        loop=False
                        speak('Access granted')
                else:
                        cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                        cv2.imshow('Face Cropper', image)
                        time.sleep(4)
                        print('NOT FOUND')
                        loop2=False
                        loop=False
                        loop3=False
                        speak('Access denied')
                        break
        except:
                cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                cv2.imshow('Face Cropper', image)
        if (cv2.waitKey(1) & 0xff) ==ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
    while loop3==True:
        if __name__=='__main__':
            greet()
            while True:
                time.sleep(2.5)
                command=orders().lower()
                if ('what is' or 'who is' or 'what are' or 'who are')  in command:
                    speak("Here's what i found!")
                    info = wikipedia.summary(command, sentences=3)
                    speak(info)
                elif ('play'and 'youtube' and 'video') in command:
                    speak('which video would you like to play?')
                    with speech_recognition.Microphone() as source10:
                                    listen_me=speech_recognition.Recognizer()
                                    listen_me.pause_threshold=1
                                    listen_me.adjust_for_ambient_noise(source10,duration=1)
                                    audio=listen_me.listen(source10)
                                    yt_video=listen_me.recognize_google(audio,language='en-in')
                    url=('https://www.youtube.com/results?search_query='+yt_video)
                    req=requests.get(url)
                    soup=bs4.BeautifulSoup(req.text,'lxml')
                    linktag=soup.select_one('a[href^="/watch"]')
                    webbrowser.open('https://www.youtube.com'+linktag.get('href'))
                elif ('open' and  'youtube') in command:
                    try:
                        print('ok')
                        webbrowser.open('https://www.youtube.com')
                        speak('I have opened')
                    except Exception:
                         print('Sorry')
                elif ('create' and  'my' and 'instagram' and 'account') in command:
                            try:
                                speak('Are you making this  account for yourself sir?')
                                with speech_recognition.Microphone() as source5:
                                        listen_me=speech_recognition.Recognizer()
                                        listen_me.pause_threshold=1
                                        listen_me.adjust_for_ambient_noise(source5,duration=1)
                                        audio=listen_me.listen(source5)
                                        input1=listen_me.recognize_google(audio,language='en-in')
                                if 'yes' or 'ofcourse' in input1:
                                            speak('What would be your username sir?')
                                            with speech_recognition.Microphone() as source8:
                                                listen_me=speech_recognition.Recognizer()
                                                listen_me.pause_threshold=1
                                                listen_me.adjust_for_ambient_noise(source8,duration=1)
                                                audio=listen_me.listen(source8)
                                                print('Recognizing!')
                                                username=listen_me.recognize_google(audio,language='en-in')
                                                username=username.replace(' ','')
                                            with speech_recognition.Microphone() as source8: 
                                                speak("Assign a password for security sir? ")
                                                listen_me.pause_threshold=1
                                                listen_me.adjust_for_ambient_noise(source8,duration=1)
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
                                            firstname=firstname.replace(' ','')
                                            with speech_recognition.Microphone() as source5: 
                                                listen_me=speech_recognition.Recognizer()
                                                listen_me.pause_threshold=1
                                                listen_me.adjust_for_ambient_noise(source5,duration=1)
                                                audio=listen_me.listen(source5)
                                                lastname=listen_me.recognize_google(audio,language='en-in')
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
                                    driver=webdriver.Chrome('your browser driver path)
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
                elif ('open' and  'instagram') in command:
                    try:
                        webbrowser.open('https://www.instagram.com')
                        speak('I have opened')
                    except Exception:
                        print('Sorry sir')
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
                        link='your news api link'
                        response=requests.get(link)
                        text=response.text
                        json_con=json.loads(text)
                        for i in range(0,5):
                          speak(json_con['articles'][i]['title'])
                    except Exception:
                        speak('Sorry sir')
                elif ("todays" and "weather") in command:
                    try:
                        link2='your weather api"s link'  
                        response=requests.get(link2)
                        text2=response.text
                        json_tem=json.loads(text2)
                        json_tem=str(json_tem['current']['temp_c'])
                        json_tem=str(json_tem + 'degree celsius')
                        print('Checking!')
                        speak(json_tem)
                    except Exception:
                        speak(' I am Sorry sir')
                elif ('login' and 'to' and  'facebook') in command:
                            try:
                                listen_me=speech_recognition.Recognizer()
                                speak('What is your  username sir!')
                                with speech_recognition.Microphone() as source24:
                                    print('Listening to you...')
                                    listen_me.pause_threshold=1
                                    listen_me.adjust_for_ambient_noise(source24,duration=1)
                                    audio=listen_me.listen(source24)
                                    username = listen_me.recognize_google(audio,language='en-in')
                                    print('Recognizing')
                                    username=username.replace(' ','')
                                    username=username.replace('p','b')
                                    username=username.lower()
                            except Exception as e:
                                print('Could not get you',e)
                            try:
                                speak('What is your password sir!!')
                                with speech_recognition.Microphone() as source36:
                                        print('Listening to you...')
                                        listen_me.pause_threshold=1
                                        listen_me.adjust_for_ambient_noise(source36,duration=1)
                                        audio=listen_me.listen(source36)
                                        password=listen_me.recognize_google(audio,language='en-in')
                                        print('Recognizing')
                                        password=password.replace(' ','')
                                        
                            except Exception as e:
                                print('could not get you',e)
                            try:
                                driver=webdriver.Chrome('your browser driver path')
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
                elif ('open' and 'facebook') in command:
                                try:
                                    webbrowser.open('https://www.facebook.com')
                                    speak("Here's your facebook")
                                except Exception:
                                    print('Sorry sir! My bad')                   
                elif ('online shopping' or 'shopping' or 'e-shopping') in command:
                    speak('What do you want to buy, sir?')
                    with speech_recognition.Microphone() as source11:
                                listen_me=speech_recognition.Recognizer()
                                listen_me.pause_threshold=1
                                listen_me.adjust_for_ambient_noise(source11,duration=1)
                                audio=listen_me.listen(source11)
                                product=listen_me.recognize_google(audio,language='en-in')
                    speak('From where would you like to buy? Amazon or Flipkart')
                    with speech_recognition.Microphone() as source12:
                            listen_me=speech_recognition.Recognizer()
                            listen_me.pause_threshold=1
                            listen_me.adjust_for_ambient_noise(source12,duration=1)
                            audio=listen_me.listen(source12)
                            site=listen_me.recognize_google(audio,language='en-in')
                    if 'Amazon' in site:
                        amazon_prod=product
                        headers={'Browser headers here'}
                        amazon_url=('https://www.amazon.com/s?k='+amazon_prod)
                        webbrowser.open(amazon_url)
                        print('GO shop')
                        time.sleep(60)
                        print('listening..')
                        with speech_recognition.Microphone() as source13:
                            listen_me=speech_recognition.Recognizer()
                            listen_me.pause_threshold=1
                            listen_me.adjust_for_ambient_noise(source13,duration=1)
                            audio=listen_me.listen(source13)
                            input10=listen_me.recognize_google(audio, language='en-in')
                        if 'set'in input10:
                            speak('set the price sir!')
                            with speech_recognition.Microphone() as source14:
                                listen_me=speech_recognition.Recognizer()
                                listen_me.pause_threshold=1
                                listen_me.adjust_for_ambient_noise(source14,duration=1)
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
                        headers={'Browser headers here}
                        flipkart_url=('https://www.flipkart.com/search?q='+flipkart_prod)
                        webbrowser.open(flipkart_url)
                        print('Happy shopping')
                        time.sleep(30)
                        print('Listening..')
                        with speech_recognition.Microphone() as source13:
                            listen_me=speech_recognition.Recognizer()
                            listen_me.pause_threshold=1 
                            listen_me.adjust_for_ambient_noise(source13,duration=1)
                            audio=listen_me.listen(source13)
                            input10=listen_me.recognize_google(audio, language='en-in')
                        if 'set price' in input10:
                            speak('set the price sir!')
                            with speech_recognition.Microphone() as source14:
                                listen_me=speech_recognition.Recognizer()
                                listen_me.pause_threshold=1
                                listen_me.adjust_for_ambient_noise(source14, duration=1)
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
                            listen_me.adjust_for_ambient_noise(source15,duration=1)
                            audio=listen_me.listen(source15)
                            input11=listen_me.recognize_google(audio, language='en-in')
                        google_url=('https://www.google.com/search?source=hp&ei=CAJIXenvHMr79QOpoLWYCA&q='+input11)
                        webbrowser.open(google_url)
                        time.sleep(7)
                        # hljtj espeak('how many suggestions should i give?')
                        # with speech_recognition.Microphone() as source16:
                        #     listen_me=speech_recognition.Recognizer()

                        #     listen_me.pause_threshold=1
                        #     listen_me.adjust_for_ambient_noise(source16,duration=1)
                        #     audio=listen_me.listen(source16)
                        #     input12=(listen_me.recognize_google(audio, language='en-in'))
                        #     input12=int(input12)
                        # req=requests.get(google_url)
                        # soup=bs4.BeautifulSoup(req.text, 'lxml')
                        # links=soup._find_one('a')
                        # linktag=min(input12,len(links))
                        # for i in range(linktag):
                        # for i in range(1):
                        
                # elif 'set my schedule' in command:
                #     speak('Tell me sir!')
                #     with speech_recognition.Microphone() as source17: 
                #             listen_me=speech_recognition.Recognizer()
                #             listen_me.pause_threshold=1
                #             listen_me.adjust_for_ambient_noise(source17, duration=1)
                #             audio = listen_me.listen(source17)
                #             schedule1=(listen_me.recognize_google(audio, language='en-in'))
                #     sched.append(schedule)
                #     with open('assistant.json','a') as file:
                #         fp=file.write(json.dump(sched))
                # elif ('my' and 'schedule') in command:
                #     with open('assistant.json','r') as file:
                #         data=file.read(json.load(sched))
                #         data=data.replace('I', 'you')
                #     for i in range(data):
                #         speak(data[i])
                elif ('open' and 'notepad') in command:
                    subprocess.Popen(['notepad.exe'])
                    time.sleep(1.8)
                    speak('Do you want me to write something for you?')
                    time.sleep(0.8)
                    with speech_recognition.Microphone() as source18:
                        listen_me=speech_recognition.Recognizer()
                        print('Listening...')
                        listen_me.pause_threshold=1
                        listen_me.adjust_for_ambient_noise(source18,duration=1)
                        audio=listen_me.listen(source18)
                        perm=listen_me.recognize_google(audio, language='en-in')
                    if 'yes' or 'ofcourse' in perm:
                        speak('Tell me what to write?')
                        with speech_recognition.Microphone() as source19:
                            listen_me=speech_recognition.Recognizer()
                            listen_me.pause_threshold=1
                            listen_me.adjust_for_ambient_noise(source19,duration=1)
                            audio=listen_me.listen(source19)
                            write1=listen_me.recognize_google(audio, language='en-in')
                        pyautogui.write(write1)
                       
                    while a=='1':
                        time.sleep(1)
                        with speech_recognition.Microphone() as source20:
                            listen_me=speech_recognition.Recognizer()
                            listen_me.pause_threshold=1
                            print('add?')
                            time.sleep(0.7)
                            listen_me.adjust_for_ambient_noise(source20,duration=1)
                            audio=listen_me.listen(source20)
                            write2=listen_me.recognize_google(audio, language='en-in')
                        if 'next line' in write2:
                            print('enter pressed')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            print('What to write in next line?')
                            with speech_recognition.Microphone() as source21:
                                listen_me=speech_recognition.Recognizer()
                                listen_me.pause_threshold=1
                                print('What to write in next line?')
                                time.sleep(0.7)
                                listen_me.adjust_for_ambient_noise(source21, duration=1)
                                audio=listen_me.listen(source21)
                                write1=listen_me.recognize_google(audio, language='en-in')
                            pyautogui.write(write1)
                        elif 'save this file' or 'safe this file' in write2:
                            time.sleep(0)
                            speak('Assign a name to the file sir?')
                            with speech_recognition.Microphone() as source22:
                                listen_me=speech_recognition.Recognizer()
                                print('assign?')
                                listen_me.pause_threshold=1
                                time.sleep(0.7)
                                listen_me.adjust_for_ambient_noise(source22, duration=1)
                                audio=listen_me.listen(source22)
                                fname=listen_me.recognize_google(audio, language='en-in')
                            pyautogui.hotkey('ctrl','s')                                                                                                                                                                                                                                                          
                            time.sleep(5)
                            pyautogui.write(fname)
                            pyautogui.hotkey('enter')
                        
                        else:
                            with speech_recognition.Microphone() as source23:
                                listen_me=speech_recognition.Recognizer()
                                listen_me.pause_threshold = 1
                                listen_me.adjust_for_ambient_noise(source23,duration=1)
                                audio=listen_me.listen(source23)
                                time.sleep(0.7)
                                write1=listen_me.recognize_google(audio, language='en-in')
                            pyautogui.write(write1)
               