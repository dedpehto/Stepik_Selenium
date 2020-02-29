from selenium import webdriver
import time

try:
    link =  "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_elements_by_css_selector('input[required].first')
#    input1.send_keys('Мой ответ')

    input2 = browser.find_elements_by_css_selector('input[required].second')
#    input2.send_keys('Мой ответ')

    input3 = browser.find_elements_by_css_selector('input[required].third')
#    input3.send_keys('Мой ответ')

    print('cовпадений input1:', len(input1), 'data:', input1[0])
    print('cовпадений input2:', len(input2), 'data:', input2[0])
    print('cовпадений input3:', len(input3), 'data:', input3[0])




    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()