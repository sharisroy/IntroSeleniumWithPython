from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demoqa.com/')
driver.maximize_window()
driver.find_element(By.XPATH, "//div/div/div[2]/div/div[1]/div/div[2]").click()
print(driver.find_element(By.XPATH, "//div/div/div[1]/div").text)  # get text of the element
driver.find_element(By.XPATH, "//div[1]/div/ul/li[1]/span").click()
print(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)

driver.find_element(By.ID, 'userName').send_keys("Haris Chandra Roy")
driver.find_element(By.ID, 'userEmail').send_keys("sharisroy@gmail.com")
driver.find_element(By.ID, 'currentAddress').send_keys("Mirpur, Dhaka")
driver.find_element(By.ID, 'permanentAddress').send_keys("Nilphamari, Rangpur, Bangladesh")
driver.execute_script("document.getElementById('submit').scrollIntoView();")
driver.find_element(By.ID, 'submit').click()
print(driver.find_element(By.ID, 'output').text)

driver.close()
