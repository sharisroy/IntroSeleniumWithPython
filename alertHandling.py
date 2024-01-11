import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import commonFunction

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demoqa.com/alerts')
driver.maximize_window()
time.sleep(3)
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)

driver.find_element(By.ID, 'alertButton').click()
alert = driver.switch_to.alert
alertTest = alert.text
print(alertTest)
time.sleep(1)
alert.accept()
time.sleep(1)

driver.find_element(By.ID, 'confirmButton').click()
alert = driver.switch_to.alert
alertTest = alert.text
print(alertTest)
time.sleep(1)
# alert.accept()
alert.dismiss()
commonFunction.print_Text(driver.find_element(By.ID, 'confirmResult').text)
time.sleep(1)

driver.find_element(By.ID, 'promtButton').click()
alert = driver.switch_to.alert
alert.send_keys("Haris Chandra Roy")
alertTest = alert.text
print(alertTest)
time.sleep(1)
alert.accept()
# alert.dismiss()
commonFunction.print_Text(driver.find_element(By.ID, 'promptResult').text)
time.sleep(1)

time.sleep(3)
driver.close()