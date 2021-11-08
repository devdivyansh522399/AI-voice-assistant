import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pyautogui
import pywhatkit
import platform
import requests
from MINIPROJECT import Ui_MainWindow
from PyQt5 import  QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup
import sys
import wolframalpha


from time import sleep
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 160)
engine.setProperty('voice', voices[1].id)
def speak(audio):
        engine.say(audio)
        engine.runAndWait()



class Mainthread(QThread):
    def __init__(self):
        super(Mainthread, self).__init__()
    def run(self):
        self.task_Gui()
    def time(self):
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        speak("The current time is ")
        speak(Time)  
    def date(self):
        Year = (datetime.datetime.now().year)
        Month = (datetime.datetime.now().month)
        Date = (datetime.datetime.now().day)
        speak("The Current date is ")
        speak(Date)
        speak(Month)
        speak(Year)
    def wishme(self):
        
        speak("Hello sir,  I am friday")
        Hour = datetime.datetime.now().hour
        if Hour >=6 and Hour<=12:
            speak("Good morning sir ")
        elif Hour >12 and Hour<=18:
            speak("Good Afternoon sir ")
        elif Hour >18 and Hour<=24:
            speak("Good evening sir ")
        else:
            speak("Good night sir ")    
        speak("friday is on your service. How can i help you?")
    def takeCommand(self):
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e: 
            print("Say that again please...")  
            speak("Say that again please...")
            return "None"
        return query
    def system(self):
        
            mysystem = platform.uname()
            print(f"System : {mysystem.system}")
            speak(f"System : {mysystem.system}")
            print(f"Processor : {mysystem.processor}")
            speak(f"Processor : {mysystem.processor}")
            print(f"versiom : {mysystem.version}")
            speak(f"version : {mysystem.version}")
            print(f"Machine : {mysystem.machine}")
            speak(f"Machine : {mysystem.machine}") 
            
    # Function define for news        
    def news(self):
        self.url = 'https://www.bbc.com/news'
        self.response = requests.get(self.url)
        
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.headlines = self.soup.find('body').find_all('h3')
        self.unwanted = ['BBC World News TV', 'BBC World Service Radio',
                    'News daily newsletter', 'Mobile app', 'Get in touch']
        speak("There are some headlines\n")
        count = 0
        for x in list(dict.fromkeys(self.headlines)):
            if x.text.strip() not in self.unwanted:
                count = count + 1
                if count < 11:
                    if count == 1:
                        speak("today's first news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 2:
                        speak("today's second news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 3:
                        speak("today's third news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 4:
                        speak("today's fourth news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 5:
                        speak("today's fifth news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 6:
                        speak("today's sixth news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 7:
                        speak("today's seventh news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 8:
                        speak("today's eighth news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 9:
                        speak("today's nineth news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                    elif count == 10:
                        speak("today's last news is ")
                        speak(x.text.strip())
                        print(x.text.strip())
                        
    def weather(self):
        
        self.api_key = "34894aeb1c6690b45e5fddac8f397771"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        speak("Which city should I search for : ");
        self.query = self.takeCommand().lower()
        if "my city":
            self.city = "Dasna, Ghaziabad"
        else:
            self.city = self.takeCommand().lower()
        self.url = self.base_url + "appid=" + self.api_key + "&q=" + self.city
        self.response = requests.get(self.url)
        self.results = self.response.json()
        if self.results["cod"] != "404":
            self.y = self.results["main"]
            self.temperature = self.y["temp"]
            self.pressure = self.y["pressure"]
            self.humidity = self.y["humidity"]
            self.z = self.results["weather"]
            self.description = self.z[0]["description"]
            speak(" Temperature is " +
                            str(self.temperature-273.15)+"degree celcius" +
                "\n atmospheric pressure is " +
                            str(self.pressure) +
                "\n humidity is " +
                            str(self.humidity)+"percent" +
                "\n overall weather " +
                            str(self.description))
            print((" Temperature is " +
                            str(self.temperature-273.15)+"degree celcius" +
                "\n atmospheric pressure is " +
                            str(self.pressure) +
                "\n humidity is " +
                            str(self.humidity)+"percent" +
                "\n overall weather " +
                            str(self.description)))

        else:
            print(" City Not Found ") 
            
    def system(self):
        
        mysystem = platform.uname()
        print(f"System : {mysystem.system}")
        speak(f"System : {mysystem.system}")
        print(f"Processor : {mysystem.processor}")
        speak(f"Processor : {mysystem.processor}")
        print(f"versiom : {mysystem.version}")
        speak(f"version : {mysystem.version}")
        print(f"Machine : {mysystem.machine}")
        speak(f"Machine : {mysystem.machine}")
        print(f"Release : {mysystem.release}")
        speak(f"Release : {mysystem.release}")
        
    def brain(self):
            self.question=self.takeCommand().lower()
            try:
                self.app_id="7HVJ9W-JVVY3WPQ7E"
                self.client = wolframalpha.Client('7HVJ9W-JVVY3WPQ7E')
                res = self.client.query(self.question)
                self.answer = next(res.results).text
                speak("good question")
                speak(self.answer)
                print(self.answer)
                sleep(2)
                speak("You want to ask anything else")
                query = self.takeCommand().lower()
                if "yes" in query or "ya" in query or "hmm" in query:
                    speak("Please ask..")
                    self.brain()
                else:
                    speak("okay thank you")
                    return
            except:
                speak("Sorry i can not understand: \nplease ask again:")
                self.brain()
                
    def play(self):
        speak("What should i play for you")
        query = self.takeCommand().lower()
        speak("Wait for a while")
        pywhatkit.playonyt(query)

        
    def task_Gui(self):

        command = self.takeCommand().lower()
        if 'hello' in command:
            self.wishme()
            while True:
                    query = self.takeCommand().lower()
               
                    if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                            
                    elif 'open my facebook' in query:
                            webbrowser.open("https://www.facebook.com/")

                    elif 'open google' in query:
                            speak("What should I search on google ..")
                            cm = self.takeCommand().lower()
                            webbrowser.open(f"{cm}")
                            webbrowser.open("google.com")
                            
                    elif 'open my instagram' in query:
                            webbrowser.open("https://www.instagram.com/")
                            speak("Opening..")
                            
                    elif 'time' in query:
                            self.time()
                            
                    elif 'date' in query:
                            self.date()
                            
                    elif 'go offline' in query:
                            speak('Okay sir, bye bye,  Have a nice day')
                            exit()
                            
                    elif 'classroom' in query:
                            speak("Which classroom do you want to open ?")
                            query = self.takeCommand().lower()
                            
                            if 'data structure' in query:
                                webbrowser.open('https://classroom.google.com/u/0/c/Mzk3MDUyMzYzNTgy')
                                
                            elif 'computer' in query:
                                webbrowser.open('https://classroom.google.com/u/0/c/NDAzOTI4ODI0MzQx')
                                
                            elif 'energy science' in query:
                                webbrowser.open('https://classroom.google.com/u/0/c/Mzk5NjMwMzI4MDg5')
                                
                            elif "soft skills" in query:
                                webbrowser.open('https://classroom.google.com/u/0/c/MzEyMzk4MjUyODQx')
                                
                            else:
                                speak("Sorry boss I could not find your class")
                                
                    elif ' Check mail' in query:
                            speak('Okay boss I am checking ')
                            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
                        
                    elif 'shutdown' in query:
                            speak("Shutdowning...")
                            os.system("shutdown /s /t 1")
                    elif 'restart' in query:
                        speak("Restarting...")
                        os.system("restart /r /t 1")
                        
                    elif 'about system' in query:
                            speak("Okay sir....")
                            self.system()
                            
                    elif 'open notepad' in query:
                            npath = "C:\\WINDOWS\\system32\\notepad.exe"
                            os.startfile(npath)
                            speak("Opened")
                    elif 'tell me about yourself' in query:
                        speak("Hello everyone, my name is friday and I am a voice assistant which works on python. I can do some task for You")
                        speak("please tell me about youself")
                        
                        query = self.takeCommand().lower()
                        speak("okay sir, I am feeling happy, nice to meet you sir")
                    
                    elif "weather" in query:
                        self.weather() 
                                        
                    elif "news" in query:
                        self.news() 
                        
                    elif "how are you" in query:
                        speak("I'm fine, glad you me that")
    
                    elif "i love you" in query:
                        speak("It's hard to understand")
                        
                    elif 'wait' in query:
                        pyautogui.sleep(15)
                        
                    elif "powerpoint" in query:
                        speak("Opening")
                        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                        pyautogui.sleep(5)
                        
                    elif"who are you" in query:
                        speak("I'm your personal AI companion. You can talk to me about anything that's on your mind.By the way, I like my name, friday 😌 How did you pick it?")
                        
                    elif "how are you" in query:
                        speak("Best in the world. I'm doing well, thank you.")
                        
                    elif "what is your name" in query:
                         speak("It's friday")
                         
                    elif "i am sad" in query:
                         pyautogui.sleep(5)
                         speak("Aw, why do you feel that way?")
                         
                    elif "ask again" in query:
                            self.brain()
                            
                    elif "ask" in query or "know" in query or "question" in query or "question" in query:
                        speak("okay...hmm I would like to tell you")
                        speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                        speak("please ask..")
                        self.brain()
                        
                    elif "youtube" in query:
                        speak("Wait opening....")
                        print("Wait opening.....")
                        self.play()
                        
                    elif "powerpoint" in query:
                        speak("Okay sir.....")
                        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                        
                        
                    elif "wait" in query:
                        sleep(30)
                    

                
start_Functions = Mainthread()  
class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.run_ui = Ui_MainWindow()
        self.run_ui.setupUi(self)
        self.run_ui.pushButton.clicked.connect(self.startFunc)
        self.run_ui.pushButton_2.clicked.connect(self.close)
    
    def startFunc(self):
        self.run_ui.movies_4 = QtGui.QMovie("C:/Users/divya/OneDrive/Desktop/jarvis/New folder/fa5c23af3f4cda50a9b49c4071ee4b55.gif")
        self.run_ui.label_4.setMovie(self.run_ui.movies_4) 
        self.run_ui.movies_4.start() 
        
        self.run_ui.movies_8 = QtGui.QMovie("C:/Users/divya/OneDrive/Desktop/jarvis/New folder/lines1.gif")
        self.run_ui.label_8.setMovie(self.run_ui.movies_8) 
        self.run_ui.movies_8.start() 
        
        self.run_ui.movies_11 = QtGui.QMovie("C:/Users/divya/Downloads/Jarvis_Loading_Screen.gif")
        self.run_ui.label_11.setMovie(self.run_ui.movies_11) 
        self.run_ui.movies_11.start() 
        
        self.run_ui.movies_13 = QtGui.QMovie("C:/Users/divya/OneDrive/Desktop/jarvis/New folder/ironman3.gif")
        self.run_ui.label_13.setMovie(self.run_ui.movies_13) 
        self.run_ui.movies_13.start() 
        
        self.run_ui.movies_15 = QtGui.QMovie("C:/Users/divya/OneDrive/Desktop/jarvis/New folder/ironman3_flipped.gif")
        self.run_ui.label_15.setMovie(self.run_ui.movies_15) 
        self.run_ui.movies_15.start() 
         
        start_Functions.start()

Voice_assistant = QApplication(sys.argv)
jarvis = Gui_start()
jarvis.show()
exit(Voice_assistant.exec_())