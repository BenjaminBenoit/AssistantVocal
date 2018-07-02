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

class MeetingCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
        self.dateFormat = "%Y %B %d %H %M"
        self.jsonFileName = "meeting_data.txt"
        self.jsonFilePath = "./meeting_data.txt"
        
        
    def getJsonDataFromJsonFile(self):
        jsonFile = Path(self.jsonFilePath)
        if(jsonFile.is_file()):
            with open(self.jsonFileName, 'r') as currentJsonFile:
                currentJsonData = json.load(currentJsonFile)
        else:
            currentJsonData = {}
        return currentJsonData
    
    
    def getMeetingDateFromUser(self):
        
        dateIsValid = False
        while(dateIsValid is not True):
            year = self.getDateElement("year");
            month = self.getDateElement("month");
            day = self.getDateElement("day");
            hour = self.getDateElement("hour");
            minute = self.getDateElement("minute");
            
            try:
                dateOfMeeting = datetime.datetime(year, month, day, hour, minute)
                dateIsValid = True
            except ValueError:
                self.speaker.say("The given date was invalid, please record it again")
                dateIsValid = False
            
        print(dateOfMeeting)
        return dateOfMeeting
    
    def getDateElement(self, elementOfDate):
        dateElement = -1
        # listener.listen return -1 if there is a Waittimeout error
        while(dateElement == -1):
            self.speaker.say("What is the number of the " + elementOfDate + " for the meeting ?")
            dateElement = self.listener.listen()
            try:
                dateElement = int(dateElement)
            except ValueError:
                self.speaker.say("The given " + elementOfDate + " is not valid.")
                dateElement = -1
        print("Element of date is " + str(dateElement))
        return dateElement
    
    
    def getMeetingSubjectFromUser(self):
        # listener.listen return -1 if there is a Waittimeout error
        subjectOfMeeting = -1
        while(subjectOfMeeting == -1):
            self.speaker.say("Please say what you want to remember at this date")
            subjectOfMeeting = self.listener.listen()
            print(subjectOfMeeting)
        return subjectOfMeeting
    
    
    def saveNewMeeting(self, dateOfMeeting, subjectOfMeeting):
        currentJsonData = self.getJsonDataFromJsonFile()
        dateOfMeetingInString = dateOfMeeting.strftime(self.dateFormat)

        if dateOfMeetingInString not in currentJsonData:
            currentJsonData[dateOfMeetingInString] = subjectOfMeeting
        else:
            currentMeetingsForDate = currentJsonData[dateOfMeetingInString]
            currentJsonData[dateOfMeetingInString] = currentMeetingsForDate + " and you also have " + subjectOfMeeting
        
        with open('meeting_data.txt', 'w+') as file:
            json.dump(currentJsonData, file, ensure_ascii=False)
                
        self.speaker.say("Meeting successfully saved")
        
        
    def executeCommand(self):
        
        self.speaker.say("Let's save a meeting!")
        
        dateOfMeeting = self.getMeetingDateFromUser()

        subjectOfMeeting = self.getMeetingSubjectFromUser()
        
        self.saveNewMeeting(dateOfMeeting, subjectOfMeeting)


        