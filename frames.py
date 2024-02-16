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

driver.get('https://demoqa.com/frames')
driver.maximize_window()
driver.implicitly_wait(3)

driver.switch_to.frame("frame2")
commonFunction.print_Text(driver.find_element(By.ID, 'sampleHeading').text)
driver.switch_to.default_content()