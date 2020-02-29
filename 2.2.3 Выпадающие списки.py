from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
#    link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

#    time.sleep(1)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')

    val = str(int(num1.text) + int(num2.text))

#    browser.find_element_by_tag_name("select").click()
#    browser.find_element_by_css_selector("[value='1']").click()
    select = Select(browser.find_element_by_tag_name("select"))


    try:
        a = select.select_by_value(val)
        a.cick()
    except:
        print("ошибка клика")

    try:
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    except:
        print("ошибка кнопки")

except:
    print('error')



#browser.close()
#browser.quit()