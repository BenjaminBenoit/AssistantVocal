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
    
    instance = None
    def __init__(self):
        if not AssistantListener.instance:
            AssistantListener.instance = AssistantListener.__AssistantListenerSingleton()
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def listen(self):
        # Important note
        # If there is too much noise in the microphone, the listener will be stuck on the listen phase
        # because he will think that the user is not done speaking (because of the noise)
        # The way to overcome this issue is to set the dynamic energy threshold at false
        # and to put the energy threshold at 400 (anythong less than that won't work)
        # !!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!! : if not using a microphone, need to set the dynamic_energy_threshold and the energy_threshold
        #self.listener.dynamic_energy_threshold = False
        #self.listener.energy_threshold = 400
        with speech_reco.Microphone(1) as source:
            print("Say something!")
            audio = self.instance.listener.listen(source, 1)
            print("Sentence recorded")
        return self.listener.recognize_google(audio)
