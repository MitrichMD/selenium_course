from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


def selenium_test(link, ver):
    print('Версия кликера: ', ver)
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(0.5)

        # кот задания
        nachat1 = browser.find_element(By.CSS_SELECTOR, "#startPlay #startPlay-img")
        nachat1.click()
        time.sleep(0.5)

        nachat2 = browser.find_element(By.CSS_SELECTOR, ".button.button_green")
        nachat2.click()
        time.sleep(0.5)

        nachat3 = browser.find_element(By.CSS_SELECTOR, ".button.button_rules")
        nachat3.click()
        time.sleep(0.5)

        pole1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Имя"]')
        pole1.send_keys("Яша")
        time.sleep(0.5)

        pole2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Почта"]')
        pole2.send_keys("malev.d@myclinic.ru")
        time.sleep(0.5)

        krugliash = browser.find_element(By.CSS_SELECTOR, ".checkbox__text")
        krugliash.click()
        time.sleep(0.5)

        nachat4 = browser.find_element(By.CSS_SELECTOR, ".button_auth")
        nachat4.click()
        time.sleep(0.5)

        for i in range(1, 1000):
            spat1 = random.uniform(0.005, 0.01)
            vizmi1 = browser.find_element(By.CSS_SELECTOR, ".button_game-action")
            vizmi1.click()
            time.sleep(spat1)

        vizmi1000 = browser.find_element(By.CSS_SELECTOR, ".button_game-action")
        vizmi1000.click()
        time.sleep(5)
        prodolz1 = browser.find_element(By.CSS_SELECTOR, ".button_lined.button_green")
        prodolz1.click()
        time.sleep(0.5)

        for i in range(1, 1500):
            spat2 = random.uniform(0.005, 0.01)
            vizmi2 = browser.find_element(By.CSS_SELECTOR, ".button_game-action")
            vizmi2.click()
            time.sleep(spat2)
        vizmi2500 = browser.find_element(By.CSS_SELECTOR, ".button_game-action")
        vizmi2500.click()
        time.sleep(5)
        prodolz2 = browser.find_element(By.CSS_SELECTOR, ".button_lined.button_green")
        prodolz2.click()
        time.sleep(0.5)

        for i in range(1, 3001):
            spat3 = random.uniform(0.005, 0.01)
            vizmi3 = browser.find_element(By.CSS_SELECTOR, ".button_game-action")
            vizmi3.click()
            time.sleep(spat3)

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(18000)

selenium_test("https://megazavod.friday.ru", 1)

        # sunduk_open = sunduk.get_attribute("valuex")

        # x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
        # x = x_element.text
        #y = calc(sunduk_open)
        #pole = browser.find_element(By.CSS_SELECTOR, "#answer")
        #pole.send_keys(y)
        #time.sleep(1)
        #korobka = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
        #orobka.click()
        #time.sleep(1)
        #knopka = browser.find_element(By.ID, "robotsRule")
        #knopka.click()
        #time.sleep(2)

        # Отправляем заполненную форму
        #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        #button.click()
    #finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
     #   time.sleep(99999999)
        # закрываем браузер после всех манипуляций
        #browser.quit()


# selenium_test("http://suninjuly.github.io/get_attribute.html", 0.001)
# selenium_test("http://suninjuly.github.io/registration2.html", 2)
