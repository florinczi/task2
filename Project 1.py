#import os
#import BY
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.automationtesting.in/JqueryProgressBar.html")
driver.implicitly_wait(8)
my_element = driver.find_element(By.ID, "downloadButton")
my_element.click()

#progress_element = driver.find_element(By.CLASS_NAME, "progress-label")
#print(f"{progress_element.text ==  'Completed!'}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), #Szukanie elementu
        'Complete!'
    )
)