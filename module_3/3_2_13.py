from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

correct_result = "Congratulations! You have successfully registered!"

def selenium_test(link):
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    el = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    el.send_keys("ололо")
    time.sleep(1)
    el = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    el.send_keys("ололо")
    time.sleep(1)
    el = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    el.send_keys("ололо")
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text

class TestSelenium1611(unittest.TestCase):
    def test_registration_1(self):
        self.assertEqual(selenium_test("http://suninjuly.github.io/registration1.html"), correct_result, "НИПРАШОЛ!")

    def test_registration_2(self):
        self.assertEqual(selenium_test("http://suninjuly.github.io/registration2.html"), correct_result, "НИПРАШОЛ!")

if __name__ == "__main__":
    unittest.main()
