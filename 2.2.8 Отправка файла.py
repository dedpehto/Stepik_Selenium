from selenium import webdriver

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("123@qwe.com")

    input4 = browser.find_element_by_name("file")
    input4.send_keys("/home/nekto/2.txt")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except:
    print('error')