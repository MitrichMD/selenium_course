from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def selenium_test(link, ver):
    print('Версия страницы: ', ver)
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        # Ваш код, который заполняет обязательные поля
        el = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        el.send_keys("ололо")
        el = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        el.send_keys("ололо")
        el = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        el.send_keys("ололо")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    except:
        print("NoSuchElementException")
    else:
        print('Test OK')
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()


selenium_test("http://suninjuly.github.io/registration1.html", 1)
selenium_test("http://suninjuly.github.io/registration2.html", 2)
