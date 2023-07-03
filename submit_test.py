# import necessary libraries 
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from canvas_scraper import CanvasScraper
import unittest
from unittest.mock import MagicMock

class ForceSubmitScraper(CanvasScraper):
    def __init__(self, driver_path) -> None:
        super().__init__(driver_path=driver_path)

    # This function will find and click the "Moderate This Quiz" button
    def click_moderate(self, quiz_link):
        self.driver.get(quiz_link)
        time.sleep(3)
        moderate_xpath = '//*[@id="sidebar_content"]/ul/li[2]/a'
        moderate_element = self.driver.find_element("xpath", moderate_xpath)

        # Unit test to see if the correct element was found
        self.test_click_moderate(moderate_element=moderate_element)

        # Click on the button
        moderate_element.click()
        time.sleep(3)

    # This function tests the click_moderate function
    def test_click_moderate(self, moderate_element):
        # Unit test that it found the correct element
        expected_text = " Moderate This Quiz "
        actual_text = moderate_element.text
        self.assertEqual(expected_text, actual_text)
        
    '''
    def test_click_moderate(self, quiz_link):
        # Mocking the necessary objects
        driver = MagicMock()

        # Call the function you want to test
        self.click_moderate(quiz_link, driver)

        # Assertions
        driver.get.assert_called_once_with(quiz_link)
        driver.find_element.assert_called_once_with("xpath", '//*[@id="sidebar_content"]/ul/li[2]/a')
        driver.find_element.return_value.click.assert_called_once()
    '''

    def check_box(self):
        # Try and except to check if orange box is present
        try:
            orange_box_xpath = '//*[@id="check_outstanding"]'
            self.driver.find_element("xpath", orange_box_xpath)
            print("found orange box")
        except:
            print("no outstanding submissions")


def main():
    # Initialize Webdriver
    options = EdgeOptions()
    options.use_chromium = True

    # provide the path to the installed webdriver here:
    driver_path = r"C:\Users\calvi\OneDrive\Documents\OnRamps\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=driver_path, options=options)

    # Give time to log in
    quiz_link = "https://onramps.instructure.com/courses/3801078/quizzes/10456211/"
    driver.get(quiz_link)
    time.sleep(30)  

    click_moderate(quiz_link=quiz_link, driver=driver)
    test_click_moderate(quiz_link=quiz_link)
    check_box(driver)

main()