# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

from Speaker import AssistantSpeaker
from WeatherCommand import WeatherCommand
from MeetingCommand import MeetingCommand
from AllCommandsCommand import AllCommandsCommand
from RemindMeetingsCommand import RemindMeetingsCommand
from ChangeParametersCommand import ChangeParametersCommand


class CommandHandler:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.weatherCommand = WeatherCommand()
        self.meetingCommand = MeetingCommand()
        self.remindMeetingsCommand = RemindMeetingsCommand()
        self.allCommandsCommand = AllCommandsCommand()
        self.changeParameterCommands = ChangeParametersCommand()
            
    def executeCommand(self, sentenceSaidByUser):
        print(sentenceSaidByUser)
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        if(sentenceSaidByUser == "weather"):
            self.weatherCommand.executeCommand()
        elif(sentenceSaidByUser == "all commands"):
            self.allCommandsCommand.executeCommand()
        elif(sentenceSaidByUser == "save meeting"):
            self.meetingCommand.executeCommand()
        elif(sentenceSaidByUser == "remind meetings"):
            self.remindMeetingsCommand.executeCommand()
        elif(sentenceSaidByUser == "change parameters"):
            self.changeParameterCommands.executeCommand()
        else:
            self.speaker.say("Sorry, I don't recognize this command. To get all the available commands, say all commands.")
            print("I don't understand")