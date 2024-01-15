from selenium.webdriver.common.by import By
import time
import math
import pytest


with open('C:/selenium_course/misc/lp.txt', 'r') as lp:
    login = lp.readline()
    password = lp.readline()

words = []
@pytest.mark.parametrize('link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_login_successful(browser, link):
    browser.implicitly_wait(10)
    browser.get(f'https://stepik.org/lesson/{link}/step/1')
    # time.sleep(3)
    login_button_1 = browser.find_element(By.CSS_SELECTOR, "#ember33")
    login_button_1.click()
    # time.sleep(1)
    email_field = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    email_field.send_keys(login)
    # time.sleep(1)
    pass_field = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    pass_field.send_keys(password)
    # time.sleep(1)
    login_button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button_2.click()
    # time.sleep(5)
    try:
        refresh_test = browser.find_element(By.CLASS_NAME, "again-btn.white")
        refresh_test.click()
        time.sleep(3)
        click_okey = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="modal-popup__container"]/footer/button[1]')))
        click_okey.click()
    except:
        pass
    # browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    answer_field = browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea")
    answer_field.send_keys(answer)
    # time.sleep(1)
    answer_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    answer_button.click()
    # time.sleep(3)
    feedback = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    word = feedback.text
    print()
    print(word)
    if word != 'Correct!':
        words.append(word)
    print()
    print("ОТВЕТ: ", *words)
