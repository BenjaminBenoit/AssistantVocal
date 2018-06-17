# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

from Speaker import AssistantSpeaker
from WeatherCommand import WeatherCommand

class CommandHandler:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.weatherCommand = WeatherCommand()
            
    def executeCommand(self, sentenceSaidByUser):
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        if(sentenceSaidByUser == "weather"):
            self.weatherCommand.executeCommand()
        else:
            self.speaker.say("Sorry, I don't recognize this command")
            print("I don't understand")