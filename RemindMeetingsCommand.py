# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

import datetime
import Constants

from Util import JsonFileUtil
from Speaker import AssistantSpeaker
from Listener import AssistantListener

class RemindMeetingsCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
        self.dateFormat = Constants.MEETING_DATE_FORMAT
        self.appJsonFile = JsonFileUtil(Constants.APP_PROPERTIES_FILENAME, Constants.APP_PROPERTIES_PATH)
        self.meetingJsonFile = JsonFileUtil(Constants.MEETING_FILENAME, Constants.MEETING_FILEPATH)
        self.intervalMeetingReminderKey = Constants.APP_PROP_INTERVALMEETING_PARAM
        
    # The app_properties file contain all the properties for the app
    # Return the number of days before a meeting we want the reminder to be triggered
    def getIntervalMeetingReminder(self):
        appProperties = self.getJsonDataFromJsonFile(self.jsonAppFilePath, self.jsonAppFileName)
        return appProperties[self.intervalMeetingReminderKey]

        
    def remindScheduledMeetings(self, numberOfDaysBeforeMeetingReminder):
        currentDate = datetime.date.today()
        maximumDateForReminder = currentDate + datetime.timedelta(days=int(numberOfDaysBeforeMeetingReminder))
        meetings = self.meetingJsonFile.getData()
        for meetingKey in meetings:
            meetingDateTime = datetime.datetime.strptime(meetingKey, self.dateFormat)
            meetingDate = meetingDateTime.date()
            # The date comparison can only be made on datetime.date objects and not on datetime.datetime!
            if(maximumDateForReminder >= meetingDate and meetingDate >= currentDate):
                meetingValue = self.meetingJsonFile.getValue(meetingKey)
                self.speaker.say(meetingValue + ' is due for ' + meetingKey)
        self.speaker.say("All the meetings coming in the next " + numberOfDaysBeforeMeetingReminder + " days have been said")
        
    def executeCommand(self):
        self.speaker.say("Reminding the upcoming meetings.")
        numberOfDaysBeforeMeetingReminder = self.appJsonFile.getValue(self.intervalMeetingReminderKey)
        self.remindScheduledMeetings(numberOfDaysBeforeMeetingReminder)       