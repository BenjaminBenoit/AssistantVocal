# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
import json
import Constants
from Util import JsonFileUtil
from Speaker import AssistantSpeaker
from Listener import AssistantListener

class ChangeParametersCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
        self.parametersJsonFile = JsonFileUtil(Constants.APP_PROPERTIES_FILENAME, Constants.APP_PROPERTIES_PATH)
            
    def executeCommand(self):
        self.speaker.say("Which application parameter would you like to change ?")
        parameter_name = self.listener.listen()
        print(parameter_name)
        if parameter_name == Constants.APP_PROP_INTERVALMEETING_PARAM:
            self.getNewParamValueAndSaveIt(parameter_name)
        elif parameter_name == Constants.APP_PROP_USERNAME_PARAM or parameter_name == 'username':
            self.getNewParamValueAndSaveIt(Constants.APP_PROP_USERNAME_PARAM)
        else:
            self.speaker.say("Sorry this parameter doesn't exist. The existing parameters are : interval meeting reminder and user name")

    def getNewParamValueAndSaveIt(self, parameter_name):
        self.speaker.say("What is the new value of this parameter ?")
        parameter_new_value = self.listener.listen()
        self.saveNewParameterValue(parameter_name, parameter_new_value)
            
    def saveNewParameterValue(self, parameter_name, parameterValue):
        currentJsonData = self.parametersJsonFile.getData()
        currentJsonData[parameter_name] = parameterValue
        
        with open(Constants.APP_PROPERTIES_FILENAME, 'w+') as file:
            json.dump(currentJsonData, file, ensure_ascii=False)
                
        self.speaker.say("New value for parameter successfully saved")
