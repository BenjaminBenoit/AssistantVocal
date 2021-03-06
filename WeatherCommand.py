# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:41:38 2018

@author: Benjamin Rosa
"""
import Constants
from bs4 import BeautifulSoup
from selenium import webdriver
from Speaker import AssistantSpeaker

class WeatherCommand:
    
    def __init__(self):
        self.speaker = AssistantSpeaker()
            
    def executeCommand(self):
        self.speaker.say("Looking for the current temperature in Montreal")
        
        # Need to specify the headless option otherwise selenium will open
        # a chrome window and we don't want that
        # Cannot use urllib here because span content is dynamic
        options = webdriver.ChromeOptions()
        options.add_argument(Constants.DRIVER_ARGUMENT)
        driver = webdriver.Chrome(executable_path=Constants.DRIVER_EXEC_PATH, chrome_options=options)
        driver.get(Constants.WEATHER_URL)
        
        # Use beautiful soup to parse the html page to speed up the process
        # Beautiful soup has a faster parser than Selenium
        beautiful_soup = BeautifulSoup(driver.page_source, Constants.BEAUTIFUL_SOUP_PARSER)
        spanWithTemperature = beautiful_soup.find_all('span', {'class' : 'temp'})[0]
        print(spanWithTemperature.text)
  
        self.speaker.say("The temperature is currently " + spanWithTemperature.text + "degree")
        print('Quit driver')
        # Important to close the driver to avoid having multiple chrome tasks
        # opened at the same time        
        driver.quit()