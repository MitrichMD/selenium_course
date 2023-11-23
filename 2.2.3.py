from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def selenium_test(link, ver):
    print('Версия страницы: ', ver)
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # кот задания
        num1 = browser.find_element(By.ID, "num1").text
        num2 = browser.find_element(By.ID, "num2").text
        num3 = int(num1) + int(num2)

        from selenium.webdriver.support.select import Select
        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_visible_text(str(num3))

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()

selenium_test("http://suninjuly.github.io/selects1.html", 1)
selenium_test("http://suninjuly.github.io/selects2.html", 1)
