# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
import json
import datetime

from pathlib import Path
from Speaker import AssistantSpeaker
from Listener import AssistantListener

class RemindMeetingsCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
        self.dateFormat = "%Y %B %d %H %M"
        self.jsonAppFileName = "app_properties.txt"
        self.jsonAppFilePath = "./app_properties.txt"
        self.intervalMeetingReminderKey = "interval meeting reminder"
        self.jsonMeetingFileName = "meeting_data.txt"
        self.jsonMeetingFilePath = "./meeting_data.txt"
        
    def getJsonDataFromJsonFile(self, jsonFilePath, jsonFileName):
        jsonFile = Path(jsonFilePath)
        if(jsonFile.is_file()):
            with open(jsonFileName, 'r') as currentJsonFile:
                appProperties = json.load(currentJsonFile)
        else:
            appProperties = {}
        return appProperties
        
    # The app_properties file contain all the properties for the app
    # Return the number of days before a meeting we want the reminder to be triggered
    def getIntervalMeetingReminder(self):
        appProperties = self.getJsonDataFromJsonFile(self.jsonAppFilePath, self.jsonAppFileName)
        return appProperties[self.intervalMeetingReminderKey]
    
    def getMeetingsFromFile(self):
        return self.getJsonDataFromJsonFile(self.jsonMeetingFilePath, self.jsonMeetingFileName)
        
    def remindScheduledMeetings(self, numberOfDaysBeforeMeetingReminder):
        meetings = self.getMeetingsFromFile()
        currentDate = datetime.date.today()
        maximumDateForReminder = currentDate + datetime.timedelta(days=int(numberOfDaysBeforeMeetingReminder))
        for meetingKey in meetings:
            meetingDateTime = datetime.datetime.strptime(meetingKey, self.dateFormat)
            meetingDate = meetingDateTime.date()
            # The date comparison can only be made on datetime.date objects and not on datetime.datetime!
            if(maximumDateForReminder >= meetingDate):
                meetingValue = meetings[meetingKey]
                self.speaker.say(meetingValue + ' is due for ' + meetingKey)
        
    def executeCommand(self):
        self.speaker.say("Reminding the upcoming meetings.")
        numberOfDaysBeforeMeetingReminder = self.getIntervalMeetingReminder()
        self.remindScheduledMeetings(numberOfDaysBeforeMeetingReminder)       