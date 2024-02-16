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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
# chrome_options.add_argument("--disable-xss-auditor")
# chrome_options.add_argument("--disable-web-security")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--allow-running-insecure-content")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-setuid-sandbox")
# chrome_options.add_argument("--disable-webgl")
# chrome_options.add_argument("--disable-popup-blocking")


# chrome_options.add_argument("--ignore-certificate-errors")

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get('https://www.google.com/')
driver.maximize_window()
commonFunction.print_Text(driver.title)
driver.implicitly_wait(3)

