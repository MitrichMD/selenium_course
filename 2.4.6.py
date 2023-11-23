from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

browser = webdriver.Chrome()
button1 = browser.find_element(By.ID, "button")
try:
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)
    #time.sleep(2)

    button1 = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
    button1.click()

    vkladka1 = browser.window_handles[0]
    vkladka2 = browser.window_handles[1]
    browser.switch_to.window(vkladka2)

    x = browser.find_element(By.ID, "input_value").text
    tgt = str(math.log(abs(12 * math.sin(int(x)))))
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(tgt)

    button2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()