import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import commonFunction

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()
driver.implicitly_wait(3)
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)
driver.find_element(By.ID,'tabButton').click()

window = driver.window_handles

driver.switch_to.window(window[1])

# commonFunction.print_Text(driver.find_element(By.ID,'sampleHeading').text)
time.sleep(3)
driver.switch_to.window(window[0])
driver.find_element(By.ID,'windowButton').click()
time.sleep(3)
driver.switch_to.window(window[1])
time.sleep(2)
commonFunction.print_Text(driver.find_element(By.ID,'sampleHeading').text)
print(len(window))