from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    #time.sleep(2)

    x = browser.find_element(By.ID, "input_value").text
    tgt = str(math.log(abs(12*math.sin(int(x)))))
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(tgt)
    #time.sleep(2)

    browser.execute_script("window.scrollBy(0, 100);")
    #time.sleep(2)

    korobka = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    korobka.click()
    #time.sleep(2)
    knopka = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    knopka.click()
    #time.sleep(2)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(20)
    browser.quit()