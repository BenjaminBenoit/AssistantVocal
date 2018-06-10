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
r = sr.Recognizer()

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
    audio = r.listen(source, 1)
    print("Sentence recorded")
    
def computerSay(sentenceToBeSaid):
        engine.say(sentenceToBeSaid)
        engine.runAndWait()
        engine.stop()    

# Recognize speech using Google Speech Recognition
try:
    # For windows, the driver is sapi5. It's nsss for OSX and espeak for other OS
    # Even if optional, need to specify the driver otherwise an error occur
    # Was needed before to init with driverName, but not anymore, check why ?
    #engine = pyttsx3.init(driverName="sapi5")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #for voice in voices:
        #print(voice, voice.id)
    # By default, the engine voice is the one of the OS (so French for me), since the command are in english, to have a 
    # good pronounciation, it's important to set the engine voice in english
    # TODO : create a separate file with methods to initialize the engine. the init method
    # should take a param like EN or FR and set the right voices
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

    sentenceSaidByUser = r.recognize_google(audio)
    
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + sentenceSaidByUser)
    if(sentenceSaidByUser == "weather"):
        computerSay("Please wait while I'm looking for the current temperature in Montreal")
        print("Prepare Selenium webdriver to get the weather")
        
        # Need to specify the headless option otherwise selenium will open
        # a chrome window and we don't want that
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chrome\chromedriver.exe", chrome_options=options)
        driver.get("https://www.meteomedia.com/ca/meteo/quebec/montreal")

        spanWithTemperature = driver.find_elements_by_xpath('.//span[@class = "temp"]')[0]
        print(spanWithTemperature.text)
        
        computerSay("The temperature is currently " + spanWithTemperature.text + "degree")      
    else:
        computerSay("I don't understand")
        print("I don't understand")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
