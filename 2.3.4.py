from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    #time.sleep(2)

    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, "input_value").text
    tgt = str(math.log(abs(12 * math.sin(int(x)))))
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(tgt)

    button2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()