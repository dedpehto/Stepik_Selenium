from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    string_x = browser.find_element_by_id('input_value')
    x = int(string_x.text)

    result = math.log(abs(12 * math.sin(x)))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



except:
    print('error')