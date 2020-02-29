from selenium import webdriver



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(9)").click()
except:
    print('error')