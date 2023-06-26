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

def click_moderate(quiz_link, driver) -> None:
    driver.get(quiz_link)
    time.sleep(3)
    driver.find_element("xpath", '//*[@id="sidebar_content"]/ul/li[2]/a').click()
    time.sleep(3)  

def check_box(driver):
    # Try and except to check if orange box is present
    try:
        driver.find_element("xpath", '//*[@id="check_outstanding"]')
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
    check_box(driver)

main()