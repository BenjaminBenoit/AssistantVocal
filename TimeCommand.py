# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

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
        print(city)
        self.speaker.say("Please wait while I'm looking for the current time in " + city)
        print("Prepare Selenium webdriver to get the time")
        
        string_current_time_city = self.getTimeFromWebSite(city)
        
        self.speaker.say("In " + city + " it is " + string_current_time_city + " o'clock.")
        
    def getTimeFromWebSite(self, city):
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chrome\chromedriver.exe", chrome_options=options)
        driver.get("https://www.timeanddate.com/worldclock/?query="+city)
        
        # Use beautifulSoup to parse the source page for better performance
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        answer = soup.find('td', id='p0')
        
        print('Quit driver')
        # Important to close the driver to avoid having multiple chrome tasks
        # opened at the same time        
        driver.quit()
        
        # Date is with format 'Day Hour:Minute AM'
        splited_answer = answer.text.split()
        return splited_answer[1] + ' ' + splited_answer[2]