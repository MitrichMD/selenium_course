from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def selenium_test(link, ver):
    print('Версия страницы: ', ver)
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # кот задания
        x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
        x = x_element.text
        y = calc(x)
        pole = browser.find_element(By.CSS_SELECTOR, "#answer")
        pole.send_keys(y)
        korobka = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
        korobka.click()
        knopka = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
        knopka.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


selenium_test("https://suninjuly.github.io/math.html", 1)
#selenium_test("http://suninjuly.github.io/registration2.html", 2)
