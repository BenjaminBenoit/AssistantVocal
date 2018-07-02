# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

from PyQt5.QtCore import QThread, pyqtSignal
from Speaker import AssistantSpeaker
from Listener import AssistantListener
from CommandHandler import CommandHandler

# Thread used to run a command in an asynchronous way
class StartActionThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    
    def __init__(self, command=None):
        QThread.__init__(self)
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
        self.commandHandler = CommandHandler()
        self.command = command
        
    def run(self):
        
        if self.command is None:
            self.speaker.say("Tell me your command")
            self.command = self.listener.listen()
        
        # -1 means a WaitTimeoutException occured
        if(self.command == -1):
            self.speaker.say("Sorry, I could not understand the command")
        else:
            self.commandHandler.executeCommand(self.command)
        
        self.signal.emit("finished")