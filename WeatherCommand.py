# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""

from selenium import webdriver
from Speaker import AssistantSpeaker

class WeatherCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
            
    def executeCommand(self):
        self.speaker.say("Looking for the current temperature in Montreal")

        print("Prepare Selenium webdriver to get the weather")
        
        # Need to specify the headless option otherwise selenium will open
        # a chrome window and we don't want that
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chrome\chromedriver.exe", chrome_options=options)
        driver.get("https://www.meteomedia.com/ca/meteo/quebec/montreal")
        
        spanWithTemperature = driver.find_elements_by_xpath('.//span[@class = "temp"]')[0]
        print(spanWithTemperature.text)
  
        self.speaker.say("The temperature is currently " + spanWithTemperature.text + "degree")
        print('Quit driver')
        # Important to close the driver to avoid having multiple chrome tasks
        # opened at the same time        
        driver.quit()