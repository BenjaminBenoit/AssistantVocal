# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

import pyttsx3
import speech_recognition as sr

# This class is used for the assistant to speak to the user
# It is a singleton
class AssistantSpeaker:
    class __AssistantSpeakerSingleton:
        def __init__(self):
            try:
                # For windows, the driver is sapi5. It's nsss for OSX and espeak for other OS
                # Even if optional, need to specify the driver otherwise an error occur
                # Was needed before to init with driverName, but not anymore, check why ?
                self.engine = pyttsx3.init(driverName="sapi5")
                self.engine = pyttsx3.init()

                # By default, the engine voice is the one of the OS (so French for me), since the command are in english, to have a 
                # good pronounciation, it's important to set the engine voice in english
                # TODO : create a separate file with methods to initialize the engine. the init method
                # should take a param like EN or FR and set the right voices
                self.engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    instance = None
    def __init__(self):
        if not AssistantSpeaker.instance:
            AssistantSpeaker.instance = AssistantSpeaker.__AssistantSpeakerSingleton()
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def say(self, sentenceToBeSaid):
        AssistantSpeaker.instance.engine.say(sentenceToBeSaid)
        AssistantSpeaker.instance.engine.runAndWait()
        AssistantSpeaker.instance.engine.stop()
