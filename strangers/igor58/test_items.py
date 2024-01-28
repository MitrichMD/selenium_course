import time
import selenium.common
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button(browser):
    browser.get(link)
    try:
        browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    except selenium.common.NoSuchElementException:
        assert False, "Button not found!"
    finally:
        time.sleep(5)
