# Importing webdriver from Selenium Web Automation Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from time import sleep
import random
import json

comments = [
    "Wanna see my n*d! pics? link in bio!",
    "I'm going na#ed, Link in bio",
    "I'm an upcoming pawn star, Support me please. Link in bio",
    "I'm an upcoming pawn star, Support me please. Link in bio",
    "I'm an upcoming pawn star, Support me please. Link in bio",
    "I'm an upcoming pawn star, Support me please. Link in bio"
]

def comment(userId, password, keyword, mssg) :
    i=0
    browser = webdriver.Chrome()
    browser.get("https://twitter.com/i/flow/login")
    sleep(5)
    userIdField = browser.find_element(By.CSS_SELECTOR, "input").send_keys(userId)
    sleep(5)
    browser.find_elements(By.CSS_SELECTOR, "div[role='button']")[2].send_keys(Keys.ENTER)
    sleep(5)
    passwordField = browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
    sleep(5)
    browser.find_elements(By.CSS_SELECTOR, "div[role='button']")[2].send_keys(Keys.ENTER)
    sleep(20)
    browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(keyword)
    sleep(4)
    browser.find_element(By.CSS_SELECTOR, "form").submit()
    sleep(7)
    
    articles = browser.find_elements(By.CSS_SELECTOR, "article")
    sleep(10)
    scrollTo = 0


    for i in range(1) :
        browser.execute_script(f"window.scrollTo(0, {str(scrollTo)})")
        articles[i].click()
        sleep(10)
        browser.find_element(By.CSS_SELECTOR, "div[contenteditable='true']").send_keys(mssg)
        sleep(10)
        browser.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']").click()
        sleep(10)
        browser.find_element(By.CSS_SELECTOR, "main div[aria-label='Back']").click()
        scrollTo = int(scrollTo) + 700
        sleep(10)
        browser.find_element(By.CSS_SELECTOR, "form").submit()
        sleep(7)
        articles = browser.find_elements(By.CSS_SELECTOR, "article")
        sleep(400)
        i+=1

    driver.quit()

with open("auth.json", 'r') as f :
    data = json.loads(f.read())
    for account in data : 
        user = account["userId"]
        psswrd = account["password"]
        cmnt = random.choice(comments)
        comment(user,psswrd,"dating",cmnt)



