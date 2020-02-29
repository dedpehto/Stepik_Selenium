from selenium import webdriver
import time
import names

#Генерируем случайные имя, фамилию, почту. Эти переменные потом вставим в найденные элементы
name = names.get_first_name()
lastname = names.get_last_name()
email = name + '.' + lastname + "@gmail.com"

# Основой код
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск и ввод имени
    input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    input1.send_keys(name)

    # Поиск и ввод фамилии
    input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    input2

    # Поиск и ввод email
    input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
    input3.send_keys(email)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()