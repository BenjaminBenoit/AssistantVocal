# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
import Constants
from bs4 import BeautifulSoup
from selenium import webdriver
from Speaker import AssistantSpeaker
from Listener import AssistantListener

class TimeCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
        self.listener = AssistantListener()
            
    def executeCommand(self):
        self.speaker.say("For which city do you want the current time ?")
        city = self.listener.listen()
        if city == -1:
            self.speaker.say("Sorry I did not understand the name of the city.")
            return -1
        print(city)
        self.speaker.say("Please wait while I'm looking for the current time in " + city)
        print("Prepare Selenium webdriver to get the time")
        
        string_current_time_city = self.getTimeFromWebSite(city)
        
        self.speaker.say("In " + city + " it is " + string_current_time_city + " o'clock.")
        
    def getTimeFromWebSite(self, city):
        
        options = webdriver.ChromeOptions()
        options.add_argument(Constants.DRIVER_ARGUMENT)
        driver = webdriver.Chrome(executable_path=Constants.DRIVER_EXEC_PATH, chrome_options=options)
        driver.get(Constants.TIME_URL + city)
        
        # Use beautifulSoup to parse the source page for better performance
        soup = BeautifulSoup(driver.page_source, Constants.BEAUTIFUL_SOUP_PARSER)
        answer = soup.find('td', id='p0')
        
        print('Quit driver')
        # Important to close the driver to avoid having multiple chrome tasks
        # opened at the same time        
        driver.quit()
        
        # Date is with format 'Day Hour:Minute AM'
        splited_answer = answer.text.split()
        return splited_answer[1] + ' ' + splited_answer[2]