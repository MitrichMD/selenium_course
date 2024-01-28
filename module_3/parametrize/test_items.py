from selenium.webdriver.common.by import By
import selenium.common
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_has_addtobasket_button(browser):
    try:
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    except selenium.common.NoSuchElementException:
        assert False, "Кнопка не найдена"
    finally:
        time.sleep(5)