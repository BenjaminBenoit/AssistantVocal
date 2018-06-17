# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
# USEFUL SHORTCUT FOR SPYDER AND OR PYTHON
# switch from editor to console : ctrl+shift+e // ctrl+shift+i
# comment several lines : ctrl+4
# comment one line : ctrl+1
#############################################

# TODO : this file should only contain what is necesary to boot the application
# create separate file and class to initialize the engine and bootstrap the app
# and when time is due : clean the comments


# Pyaudio API : http://people.csail.mit.edu/hubert/pyaudio/docs/
import pyaudio
import pyttsx3
from selenium import webdriver
import speech_recognition as sr

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    
    def __init__(self, recognizer, engine):
        super().__init__()
        self.title = 'Personal Assistant'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        self.recognizer = recognizer
        self.engine = engine
 
    def initUI(self):
        
        # Initialize window running the app
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Start the application at the center of the screen
        qtRectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(center_point)
        self.move(qtRectangle.topLeft())
 
        # Initialize start button
        start_button = QPushButton('Start', self)
        start_button.resize(200, 50)
        start_button.move(60,75)
        start_button.setStyleSheet('font:bold;font-size:30px;')
        start_button.clicked.connect(self.on_start_click)
 
        #self.setStyleSheet('background-image: url(background.jpg);')
        self.show()
        
    def computerSay(self, sentenceToBeSaid):
            self.engine.say(sentenceToBeSaid)
            self.engine.runAndWait()
            self.engine.stop()
            
    def executeCommand(self, sentenceSaidByUser):
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        #print("Google Speech Recognition thinks you said " + sentenceSaidByUser)
        if(sentenceSaidByUser == "weather"):
            self.computerSay("Please wait while I'm looking for the current temperature in Montreal")
            print("Prepare Selenium webdriver to get the weather")
            
            # Need to specify the headless option otherwise selenium will open
            # a chrome window and we don't want that
            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chrome\chromedriver.exe", chrome_options=options)
            driver.get("https://www.meteomedia.com/ca/meteo/quebec/montreal")
    
            spanWithTemperature = driver.find_elements_by_xpath('.//span[@class = "temp"]')[0]
            print(spanWithTemperature.text)
            
            self.computerSay("The temperature is currently " + spanWithTemperature.text + "degree")
            
            # Important to close the driver to avoid having multiple chrome tasks
            driver.quit()
    
        else:
            self.computerSay("Sorry, I don't recognize this command")
            print("I don't understand")
        
 
    @pyqtSlot()
    def on_start_click(self):
        self.computerSay("Tell me your command")
        # Important note
        # If there is too much noise in the microphone, the recognizer will be stuck on the listen phase
        # because he will think that the user is not done speaking (because of the noise)
        # The way to overcome this issue is to set the dynamic energy threshold at false
        # and to put the energy threshold at 400 (anythong less than that won't work)
        # !!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!! : if not using a microphone, need to set the dynamic_energy_threshold and the energy_threshold
        #r.dynamic_energy_threshold = False
        #r.energy_threshold = 400
        with sr.Microphone(1) as source:
            print("Say something!")
            audio = self.recognizer.listen(source, 1)
            print("Sentence recorded")
        sentenceSaidByUser = self.recognizer.recognize_google(audio)
        self.executeCommand(sentenceSaidByUser)
        
if __name__ == '__main__':
    
    # =============================================================================
    # for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    # =============================================================================
    print("=== Initializing pyaudio")
    pyaudio.pa.initialize()
    print("=== Initializing text to speech engine")
    
    print("=== Number of devices : ")
    print(pyaudio.pa.get_device_count())
    print("=== Index of default input device : ")
    print(pyaudio.pa.get_default_input_device())
    
    # NOTE: this example requires PyAudio because it uses the Microphone class
    
    # obtain audio from the microphone
    recognizer = sr.Recognizer()
    
    # Recognize speech using Google Speech Recognition
    try:
        # For windows, the driver is sapi5. It's nsss for OSX and espeak for other OS
        # Even if optional, need to specify the driver otherwise an error occur
        # Was needed before to init with driverName, but not anymore, check why ?
        engine = pyttsx3.init(driverName="sapi5")
        engine = pyttsx3.init()
        #voices = engine.getProperty('voices')
        #for voice in voices:
            #print(voice, voice.id)
        # By default, the engine voice is the one of the OS (so French for me), since the command are in english, to have a 
        # good pronounciation, it's important to set the engine voice in english
        # TODO : create a separate file with methods to initialize the engine. the init method
        # should take a param like EN or FR and set the right voices
        engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    app = QApplication(sys.argv)
    ex = App(recognizer, engine)
    sys.exit(app.exec_())

