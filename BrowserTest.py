from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")
driver.maximize_window();
title = driver.title
print(title)

assert "Selenium" in title

driver.close()  # close only current windows
# driver.quit()  # kill the browser session
