# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""


from Speaker import AssistantSpeaker

class AllCommandsCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
            
    def executeCommand(self):
        self.speaker.say("The available commands are : All commands, Change parameters, Help, Save meeting, Remind meetings and Weather. For more informations about a command, say help.")
        

        