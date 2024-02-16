# mouse hover
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

driver.get('https://demoqa.com/menu')
driver.maximize_window()
driver.implicitly_wait(3)
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)
# Move to Element
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')).perform()
action.move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')).perform()
commonFunction.print_Text(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[1]/a').text)
action.move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[1]/a')).click().perform()
commonFunction.print_Text(driver.current_url)
wait = WebDriverWait(driver, 5)  # the alert is present after 5 seconds. Explicit wait
# wait.until(expected_conditions.alert_is_present())

# Drag and Drop

driver.get("https://demoqa.com/droppable")
time.sleep(3)
action.drag_and_drop(driver.find_element(By.ID, 'draggable'), driver.find_element(By.ID, 'droppable')).perform()
commonFunction.print_Text(driver.find_element(By.XPATH, '//*[@id="droppable"]/p').text)
commonFunction.print_Text(driver.find_element(By.XPATH, '//*[@id="droppable"]').get_attribute("class"))

time.sleep(3)

driver.close()
