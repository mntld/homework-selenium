from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # Открыть страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, пока цена снизится до $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # Решаем задачу
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    browser.find_element(By.ID, "answer").send_keys(answer)

    # Отправляем результат
    browser.find_element(By.ID, "solve").click()

    # Считываем число
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    time.sleep(5)
    browser.quit()
