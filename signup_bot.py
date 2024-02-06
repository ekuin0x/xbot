from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.mohmal.com/en")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "#rand").click()
time.sleep(100)
driver.quit()