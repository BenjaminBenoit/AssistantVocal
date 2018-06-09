# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Admin
"""
# USEFUL SHORTCUT FOR SPYDER AND OR PYTHON
# switch from editor to console : ctrl+shift+e // ctrl+shift+i
# comment several lines : ctrl+4
# comment one line : ctrl+1
#############################################

# TODO : this file should onlu contain what is necesary to boot the application
# create separate file and class to initialize the engine and bootstrap the app
# and when time is due : clean the comments

import webbrowser
import string
import torch
# Pyaudio API : http://people.csail.mit.edu/hubert/pyaudio/docs/
import pyaudio
import pyttsx3
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


# obtain audio
# https://stackoverflow.com/questions/42184876/google-speech-recognition-api-not-listening
"""
r = sr.Recognizer()
with sr.AudioFile("microphone-results.wav") as source:
    audio = r.listen(source)
print("START GOOGLE API")
print(r.recognize_google(audio))
print("FINI")
"""

"""
r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 48000) as source:
    audio = r.record(source, duration = 5)
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
    """

"""
r = sr.Recognizer()
with sr.Microphone(1) as source:
   print("Hello what can i help you find?")
   audio = r.listen(source)
   print("OK")
   
print(r.recognize_google(audio))
print("test print")
"""

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

# obtain audio from the microphone
r = sr.Recognizer()

# Important note
# If there is too much noise in the microphone, the recognizer will be stuck on the listen phase
# because he will think that the user is not done speaking (because of the noise)
# The way to overcome this issue is to set the dynamic energy threshold at false
# and to put the energy threshold at 400 (anythong less than that won't work)
# IMPORTANT : if not using a microphone, those 2 lines need to be uncomment
#r.dynamic_energy_threshold = False
#r.energy_threshold = 400
with sr.Microphone(1) as source:
    print("Say something!")
    audio = r.listen(source, 1)
    print("Sentence recorded")



# recognize speech using Sphinx
""" Pocket sphynx is not working at the moment
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
"""

# recognize speech using Google Speech Recognition
try:
    # For windows, the driver is sapi5. It's nsss for OSX and espeak for other OS
    # Even if optional, need to specify the driver otherwise an error occur
    # Was needed before to init with driverName, but not anymore, check why ?
    #engine = pyttsx3.init(driverName="sapi5")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice, voice.id)
    # By default, the engine voice is the one of the OS (so French for me), since the command are in english, to have a 
    # good pronounciation, it's important to set the engine voice in english
    # TODO : create a separate file with methods to initialize the engine.
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

            
    
    sentenceSaidByUser = r.recognize_google(audio)
    
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + sentenceSaidByUser)
    if(sentenceSaidByUser == "weather"):
        engine.say("You said weather")
        engine.runAndWait()
        engine.stop()
        print("Use scrappy to get the weather")
    else:
        engine.say("I don't understand")
        engine.runAndWait()
        engine.stop()
        print("I don't understand")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))





# recognize speech using Google Cloud Speech
"""
GOOGLE_CLOUD_SPEECH_CREDENTIALS = INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
"""
