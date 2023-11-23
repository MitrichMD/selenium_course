from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element([By.ID, 'price'], '$100')
    )
    button.click()

    #vkladka1 = browser.window_handles[0]
    #kladka2 = browser.window_handles[1]
    #browser.switch_to.window(vkladka2)

    x = browser.find_element(By.ID, "input_value").text
    tgt = str(math.log(abs(12 * math.sin(int(x)))))
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(tgt)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(60)
    browser.quit()