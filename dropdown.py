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

driver.get('https://demoqa.com/select-menu')
driver.maximize_window()
time.sleep(3)
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)

# Static Dropdown
# dropdown = Select(driver.find_element(By.ID,'oldSelectMenu'))
# dropdown.select_by_index(5)
# time.sleep(2)
# dropdown.select_by_value("10")
# time.sleep(2)
# dropdown.select_by_visible_text("Green")

#Input and select option
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# driver.find_element(By.XPATH,'//div[7]/div/div/div/div[1]').click()
# time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="react-select-4-input"]').send_keys('e')
# time.sleep(2)
# color = driver.find_elements(By.XPATH,'//div[7]/div/div/div/div[1]/div')
# for c in color:
#     commonFunction.print_Text(c.text)
#     if c.text == 'Red':
#         c.click()
#
# time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="react-select-4-input"]').send_keys('b')
# time.sleep(2)
# color = driver.find_elements(By.XPATH,'//div[7]/div/div/div/div[1]/div')
# for c in color:
#     commonFunction.print_Text(c.text)
#     if c.text == 'Black':
#         c.click()

# commonFunction.print_Text(driver.find_element(By.XPATH,'//div[7]/div/div/div/div[1]').get_attribute('value'))

driver.find_element(By.XPATH,'//*[@id="selectOne"]').click()
time.sleep(2)
p = driver.find_elements(By.XPATH, '//*[@id="selectOne"]/div[2]/div/div/div/div')
print(len(p))
for t in p:
    commonFunction.print_Text(t.text)
    if t.text == 'Mrs.':
        t.click()
# print(driver.find_element(By.XPATH, '//*[@id="selectOne"]/div[2]/div/div/div/div').text)
# print(driver.find_element(By.XPATH, '//*[@id="selectOne"]/div[2]/div/div').get_property())
time.sleep(3)
driver.close()