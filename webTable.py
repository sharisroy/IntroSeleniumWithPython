from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import commonFunction

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demoqa.com/webtables')
driver.maximize_window()
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)

commonFunction.print_Text(
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]').text)

# Add new item
driver.find_element(By.ID,'addNewRecordButton').click()
commonFunction.print_Text(driver.find_element(By.ID, 'registration-form-modal').text)
driver.find_element(By.ID,'firstName').send_keys("Haris Chandra")
driver.find_element(By.ID,'lastName').send_keys("Roy")
driver.find_element(By.ID,'userEmail').send_keys("sharisroy@gmail.com")
driver.find_element(By.ID,'age').send_keys("30")
driver.find_element(By.ID,'salary').send_keys("50000")
driver.find_element(By.ID,'department').send_keys("SQA")
driver.find_element(By.ID,'submit').click()
driver.implicitly_wait(10)

driver.find_element(By.ID, 'searchBox').send_keys('Haris')
commonFunction.check_Text(
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]').text, 'Haris')


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select').click()
driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select/option[1]').click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select').click()
driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select/option[4]').click()

driver.close()
