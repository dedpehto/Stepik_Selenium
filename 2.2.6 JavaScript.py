from selenium import webdriver
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

#    time.sleep(1)

    string_x = browser.find_element_by_id('input_value')
    x = int(string_x.text)

    result = math.log(abs(12*math.sin(x)))
    print(result)

    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))


    option1 = browser.find_element_by_class_name("form-check-label")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except:
    print('error')



#browser.close()
#browser.quit()