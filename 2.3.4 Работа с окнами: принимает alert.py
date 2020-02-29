from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    string_x = browser.find_element_by_id('input_value')
    x = int(string_x.text)

    result = math.log(abs(12 * math.sin(x)))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


except:
    print('error')