# Importing webdriver from Selenium Web Automation Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
import time

def comment(userId, password, keyword, mssg) :
    browser = webdriver.Chrome()
    browser.get("https://twitter.com/i/flow/login")
    time.sleep(5)
    userIdField = browser.find_element(By.CSS_SELECTOR, "input").send_keys(userId)
    time.sleep(2)
    browser.find_elements(By.CSS_SELECTOR, "div[role='button']")[2].send_keys(Keys.ENTER)
    time.sleep(2)
    passwordField = browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
    time.sleep(2)
    browser.find_elements(By.CSS_SELECTOR, "div[role='button']")[2].send_keys(Keys.ENTER)
    time.sleep(7)
    browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "form").submit()
    time.sleep(7)
    
    articles = browser.find_elements(By.CSS_SELECTOR, "article")
    time.sleep(10)
    scrollTo = 0
    for article in articles :
        browser.execute_script(f"window.scrollTo(0, {str(scrollTo)})")
        article.click()
        time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, "div[contenteditable='true']").send_keys(mssg)
        time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']").click()
        time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, "main div[aria-label='Back']").click()
        scrollTo = int(scrollTo) + 700
        time.sleep(10)

    driver.quit()

keyword = "Dating"
mssg = "Hello World"
comment("AFabicci65289","s)H4ZJvbbe6Uv2x",keyword,mssg)


