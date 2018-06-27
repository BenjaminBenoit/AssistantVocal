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
    
    def __init__(self):
        QThread.__init__(self)
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
        self.commandHandler = CommandHandler()
        
    def run(self):
        self.speaker.say("Tell me your command")
        sentenceSaidByUser = self.listener.listen()
        
        # -1 means a WaitTimeoutException occured
        if(sentenceSaidByUser == -1):
            self.speaker.say("Sorry, I could not understand the command")
        else:
            self.commandHandler.executeCommand(sentenceSaidByUser)
            
        self.signal.emit("finished")
