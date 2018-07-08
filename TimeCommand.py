# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
import datetime
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
        print("Prepare Selenium webdriver to get the time")
        
        # Need to specify the headless option otherwise selenium will open
        # a chrome window and we don't want that
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chrome\chromedriver.exe", chrome_options=options)
        driver.get("https://www.timeanddate.com/worldclock/")
        
        inputFieldForCity = driver.find_element_by_xpath('.//input[@class="inline nine"]')
        searchButton = driver.find_element_by_xpath('.//input[@value = "Search"]')
        inputFieldForCity.click()
        inputFieldForCity.send_keys(city)
        searchButton.click()
        answer = driver.find_element_by_xpath('.//td[@id="p0"]')
        print(answer.text)
        
        # The answer is of form 'day hour h minute'. we parse it through each white space
        parse_answer = answer.text.split()
        hour = int(parse_answer[1])
        minute = int(parse_answer[3])
        city_time = datetime.time(hour, minute)
        
        # Format the hour in am-pm with %I. %p will display the AM or PM information
        am_pm_city_time = city_time.strftime('%I:%M %p')
        
        
        self.speaker.say("In " + city + " it is " + am_pm_city_time + " o'clock.")
        print('Quit driver')
        # Important to close the driver to avoid having multiple chrome tasks
        # opened at the same time        
        driver.quit()