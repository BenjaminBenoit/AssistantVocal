# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
# USEFUL SHORTCUT FOR SPYDER AND OR PYTHON
# switch from editor to console : ctrl+shift+e // ctrl+shift+i
# comment several lines : ctrl+4
# comment one line : ctrl+1
#############################################

import sys
import pyaudio
from AssistantApp import AssistantApp
from PyQt5.QtWidgets import QApplication

# Entry point of the application
if __name__ == '__main__':
    
    print("=== Initializing pyaudio")
    pyaudio.pa.initialize()
    print("=== Initializing text to speech engine")
    
    print("=== Number of devices : ")
    print(pyaudio.pa.get_device_count())
    print("=== Index of default input device : ")
    print(pyaudio.pa.get_default_input_device())
    
    app = QApplication(sys.argv)
    ex = AssistantApp(app)
    sys.exit(app.exec_())