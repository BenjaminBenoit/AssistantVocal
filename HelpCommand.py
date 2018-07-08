# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""


from Speaker import AssistantSpeaker
from Listener import AssistantListener

class HelpCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
            
    def executeCommand(self):
        self.speaker.say("For which command do you need help ?")
        command_for_help = self.listener.listen()

        if command_for_help == 'weather':
            self.speaker.say("Simply say weather and you will have the current temperature in Montreal.")
        elif command_for_help == 'change parameters':
            self.speaker.say("After saying the command name, you will be ask to say the parameter name and the parameter value.")
        elif command_for_help == 'time':
            self.speaker.say("After saying the command name, you will be ask to say the name of the city. You will then hear the current time of the most likely city found.")
        elif command_for_help == 'all commands':
            self.speaker.say("Give all the available commands in the application.")
        elif command_for_help == 'remind meetings':
            self.speaker.say("The assistant will say all the upcoming meetings the the user. All the meetings from today plus the days interval specified in the interval meeting reminder application parameter will be reminded.")
        elif command_for_help == 'save meeting':
            self.speaker.say("For saving a meeting, you need too give, when it is asked, the year, the month (using number from 1 to 12), the day (using number from 1 to 31), the hour (using number from 0 to 24), the minute (using number from 0 to 60) and the meeting content")
        else:
            self.speaker.say("Sorry this command doesn't exist. For a list of all available commands, say All commands.")