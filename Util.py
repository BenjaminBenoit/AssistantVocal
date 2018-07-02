# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

import json
from pathlib import Path


class JsonFileUtil:
    
    def __init__(self, jsonFileName, jsonFilePath):
        jsonFile = Path(jsonFilePath)
        if(jsonFile.is_file()):
            with open(jsonFileName, 'r') as currentJsonFile:
                appProperties = json.load(currentJsonFile)
        else:
            appProperties = {}
        self.appProperties = appProperties

    def getValue(self, key):
        return self.appProperties[key]
    
    def getData(self):
        return self.appProperties
        

        