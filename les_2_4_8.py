from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math,time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 15 секунд, пока цена не станет 100
WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

browser.find_element_by_class_name('btn.btn-primary').click()

x = browser.find_element_by_id('input_value').text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)

browser.find_element_by_id('solve').click()

alert = browser.switch_to_alert()
print (alert.text)
alert.accept()

browser.quit()
