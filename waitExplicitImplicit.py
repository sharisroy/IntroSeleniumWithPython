# Implicit : Wait max n seconds, if found element in 2 seconds it save (n-2) seconds
#           if it applies in the global it will wait for all elements
#           Implicit wait is not working for find by elements


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import commonFunction

# create driver object
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# A URL that delays loading
driver.get('https://demoqa.com/alerts')

try:

    driver.implicitly_wait(3)  # wait max 3 seconds. Implicit wait
    driver.maximize_window()
    commonFunction.print_Text(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div').text)
    driver.find_element(By.ID, 'timerAlertButton').click()

    wait = WebDriverWait(driver, 6)  # the alert is present after 5 seconds. Explicit wait
    wait.until(expected_conditions.alert_is_present())

    alert = driver.switch_to.alert
    alertTest = alert.text
    print(alertTest)
    alert.accept()

finally:
    # else quit
    driver.quit()
