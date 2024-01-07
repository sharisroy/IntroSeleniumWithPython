import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import commonFunction

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demoqa.com/buttons')
driver.maximize_window()
time.sleep(3)
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)

# button single click
driver.find_element(By.XPATH,'//div/div/div[2]/div[2]/div[2]/div[3]/button').click()
commonFunction.check_Text(driver.find_element(By.ID, 'dynamicClickMessage').text, 'dynamic click')

# right button click
action = ActionChains(driver)
action.context_click(driver.find_element(By.XPATH,'//div/div/div[2]/div[2]/div[2]/div[2]/button')).perform()
commonFunction.check_Text(driver.find_element(By.ID, 'rightClickMessage').text, 'right click')

# button double click
action.double_click(driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[1]/button')).perform()
commonFunction.check_Text(driver.find_element(By.ID, 'doubleClickMessage').text, 'double click')
time.sleep(3)


driver.get('https://demoqa.com/links')
time.sleep(2)
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)
driver.find_element(By.ID,'created').click()
commonFunction.check_Text(driver.find_element(By.ID, 'linkResponse').text, 'Created')

driver.find_element(By.ID,'unauthorized').click()
commonFunction.check_Text(driver.find_element(By.ID, 'linkResponse').text, 'Unauthorized')

time.sleep(2)
driver.close()