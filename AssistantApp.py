# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget
from Speaker import AssistantSpeaker
from Listener import AssistantListener
from CommandHandler import CommandHandler


class AssistantApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Personal Assistant'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
        self.commandHandler = CommandHandler()
 
    def initUI(self):
        
        # Initialize window running the app
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Start the application at the center of the screen
        qtRectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(center_point)
        self.move(qtRectangle.topLeft())
 
        # Initialize start button
        start_button = QPushButton('Start', self)
        start_button.resize(200, 50)
        start_button.move(60,75)
        start_button.setStyleSheet('font:bold;font-size:30px;')
        start_button.clicked.connect(self.on_start_click)
 
        self.show()        
 
    @pyqtSlot()
    def on_start_click(self):
        self.speaker.say("Tell me your command")
        sentenceSaidByUser = self.listener.listen()
        self.commandHandler.executeCommand(sentenceSaidByUser)

