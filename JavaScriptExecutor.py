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

driver.get('https://rahulshettyacademy.com/AutomationPractice')
driver.maximize_window()
driver.implicitly_wait(3)

# driver.execute_script("window.scrollBy(0,500)")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollBy(0,-500);")  # scroll up 500 pixel
time.sleep(3)
driver.get_screenshot_as_file("screenShot.png")
driver.close()
