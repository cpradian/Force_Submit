# import necessary libraries 
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from canvas_scraper import CanvasScraper


class ForceSubmitScraper(CanvasScraper):
    def __init__(self, driver_path, links_path):
        super().__init__(driver_path=driver_path)
        self.assignment_df = pd.read_csv(links_path)
        self.instructors = self.assignment_df["Instructor"]
        self.links = self.assignment_df["Canvas Link"]
        # Hashset filled with unique urls that have been looped through
        self.url_set = set()

    # This function will find and click the "Moderate This Quiz" button
    def click_moderate(self, quiz_link): 
        self.driver.get(quiz_link)
        time.sleep(3)
        # Get the url of 'Moderate This Quiz'
        moderate_link = quiz_link + r"/moderate"

        '''
        moderate_xpath = '//*[@id="sidebar_content"]/ul/li[2]/a'
        moderate_element = self.driver.find_element("xpath", moderate_xpath)

        # Unit test to see if the correct element was found
        self.test_click_moderate(moderate_element=moderate_element)
        '''
        try:
            # Navigate to 'Moderate This Quiz'
            self.driver.get(moderate_link)
            time.sleep(3)
        except:
            print("No 'Moderate This Quiz'")

    # This function tests the click_moderate function
    def test_click_moderate(self, moderate_element):
        # Unit test that it found the correct element
        expected_text = "Moderate This Quiz\nModerate This Quiz"
        actual_text = moderate_element.text
        assert expected_text == actual_text

    # This function checks if there is an orange box that indicates outstanding submissions
    def check_box(self):
        # Try and except to check if orange box is present
        try:
            orange_box_xpath = '//*[@id="check_outstanding"]'
            oustanding_element = self.driver.find_element("xpath", orange_box_xpath)
            # Unit test to see if the correct element was found
            self.test_check_box(outstanding_element=oustanding_element)
            print("There are outstanding submissions")
            oustanding_element.click()
            time.sleep(5)
        except:
            print("no outstanding submissions")
    
    def test_check_box(self, outstanding_element):
        # Unit test that it found the correct element
        expected_text = "Check on outstanding quiz submissions"
        print(expected_text)
        actual_text = outstanding_element.text
        assert expected_text ==  actual_text

    def submit_button(self):
        try:
            # submit_button_xpath = '//*[@id="autosubmit_form_submit_btn"]'
            submit_button_xpath = '//*[@id="autosubmit_form_submit_btn"]/span'
            submit_element = self.driver.find_element("xpath", submit_button_xpath)
            # Unit test to see if the correct element was found
            self.test_submit_button(submit_button_element=submit_element)
            submit_element.click()
            time.sleep(5)
        except:
            pass

    def test_submit_button(self, submit_button_element):
        # Unit test that it found the correct element
        expected_text = "Submit"
        actual_text = submit_button_element.text
        assert expected_text ==  actual_text

    # Use hashset to store unique urls. If the url has been added, 
    def check_duplicate_urls(self, url):
        if url in self.url_set:
            print(f"Duplicate URL found: {url}")
            return True
        else:
            self.url_set.add(url)
            return False
        
    def force_submit(self):
        # do log in process
        self.login(url=self.links[0])

        # Loop through all assignment links
        for link in self.links:
            # Check if link has already been iterated through
            if self.check_duplicate_urls(url=link):
                continue

            # Click on the "Moderate This Quiz" button
            self.click_moderate(quiz_link=link)
            
            # Check if there are outstanding submissions
            self.check_box()

            # Click the submit button if there are
            self.submit_button()
