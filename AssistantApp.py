# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QApplication
from CommandThread import StartActionThread
from Util import JsonFileUtil
from Speaker import AssistantSpeaker

# This class setup the UI part of the application
class AssistantApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Personal Assistant'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.command_thread = StartActionThread()
        self.command_thread.signal.connect(self.on_thread_finished)
        self.speaker = AssistantSpeaker()
        self.initUI()
 
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
        self.start_button = QPushButton('Start', self)
        self.start_button.resize(200, 50)
        self.start_button.move(60,75)
        self.start_button.setStyleSheet('font:bold;font-size:30px;')
        self.start_button.clicked.connect(self.on_start_click)
        
        self.welcomingUser()
        self.show()
        
    def on_thread_finished(self):
        self.start_button.setEnabled(True)
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        self.command_thread.terminate()
        self.command_thread = StartActionThread()
        self.command_thread.signal.connect(self.on_thread_finished)
 
    @pyqtSlot()
    def on_start_click(self):
        self.start_button.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.command_thread.start()
        
    def welcomingUser(self):
        jsonFile = JsonFileUtil("app_properties.txt", "./app_properties.txt")
        userName = jsonFile.getValue("user name")
        self.speaker.say("Welcome " + userName)
        