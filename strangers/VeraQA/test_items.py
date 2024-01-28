import time
import pytest
from selenium.webdriver.common.by import By



def test_add_to_cart_button_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    # Добавление задержки для визуальной проверки языка на кнопке
    time.sleep(5)

     # Проверка наличия кнопки добавления в корзину
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert add_to_basket_button.is_displayed() and add_to_basket_button.is_enabled(), 'Add to basket button is not present or not interactable.'