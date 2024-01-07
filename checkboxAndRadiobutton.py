from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import commonFunction

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demoqa.com/checkbox')
driver.maximize_window()
commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)

# driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]').click()
# commonFunction.check_Text(driver.find_element(By.XPATH, '//*[@id="result"]').text, 'home')
# driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]').click()
driver.implicitly_wait(100)
driver.find_element(By.CSS_SELECTOR, "#tree-node > ol > li > span > button > svg").click()
driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > span > button > svg').click()
driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol '
                                     '> li:nth-child(2) > span > button > svg').click()
driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol '
                                     '> li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span >'
                                     ' label > span.rct-checkbox > svg').click()
commonFunction.check_Text(driver.find_element(By.XPATH, '//*[@id="result"]').text, 'private')

driver.get('https://demoqa.com/radio-button')
driver.find_element(By.XPATH, "//div/div/div[2]/div[2]/div[2]/div[2]/label").click()
driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[3]/label').click()
driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[2]/label').click()
commonFunction.check_Text(driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/p/span').text, 'Yes')
print(driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[4]/label').is_selected())
driver.close()
