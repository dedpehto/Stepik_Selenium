from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
#    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None


    # Поиск и ввод имени
#    input1 = browser.find_element_by_id('input_value')
#    x = int(input1.text)
#    y = calc(x)

#    answer = browser.find_element_by_id('answer')
#    answer.send_keys(y)


#    option1 = browser.find_element_by_id("robotCheckbox")
#    option1.click()

#    option2 = browser.find_element_by_id("robotsRule")
#    option2.click()

#    button = browser.find_element_by_css_selector("button.btn")
#    button.click()

    browser.quit()

except:
    print('ошибка')
    browser.quit()