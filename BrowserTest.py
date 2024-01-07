from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# Chrome Browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# # Firefox Browser
# service_obj = Service()
# driver = webdriver.Firefox(service=service_obj)


driver.get("https://www.selenium.dev")
driver.maximize_window();
title = driver.title
print(title)
print(driver.current_url)
assert "Selenium" in title

driver.get("https://www.google.com")

# driver.minimize_window()
driver.fullscreen_window()
driver.back()
driver.forward()
driver.refresh()

driver.close()  # close only current windows
# driver.quit()  # kill the browser session
