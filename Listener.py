# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

import speech_recognition as speech_reco

# This class is used for the assistant to listen to the user
# It is a singleton
class AssistantListener:
    class __AssistantListenerSingleton:
        def __init__(self):
            # obtain audio from the microphone
            self.listener = speech_reco.Recognizer()
            self.microphone = speech_reco.Microphone()
    
    instance = None
    def __init__(self):
        if not AssistantListener.instance:
            print(speech_reco.Microphone.list_microphone_names())
            AssistantListener.instance = AssistantListener.__AssistantListenerSingleton()
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def listen(self):
        
        with self.microphone as source:
            self.instance.listener.adjust_for_ambient_noise(source)
            audio = self.instance.listener.listen(source)
            
        try:
            transcription = self.instance.listener.recognize_google(audio)
        except speech_reco.WaitTimeoutError:
                print("Sentence not said fast enough - WaitTimeoutError")
                return -1
        except speech_reco.UnknownValueError:
                print("Sentence said too fast - UnknownValueError")
                return -1
        except speech_reco.RequestError:
                print("An exception occured - RequestError")
                return -1 
        return transcription
