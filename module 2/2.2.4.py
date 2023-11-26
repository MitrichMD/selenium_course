from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def selenium_test(link, ver):
    print('Версия страницы: ', ver)
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # кот задания
        browser.execute_script("document.title='Script executing';alert('Robots at work');")

    finally:
        time.sleep(5)
        browser.quit()


selenium_test("https://suninjuly.github.io/execute_script.html", 1)
