from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    #time.sleep(2)

    el = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    el.send_keys("ололо")
    el = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    el.send_keys("ололо")
    el = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    el.send_keys("ололо")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'ololo.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    #element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
finally:
    time.sleep(20)
    browser.quit()