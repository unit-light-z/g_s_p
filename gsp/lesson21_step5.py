from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    xx = browser.find_element_by_xpath("//span[@id='input_value']")
    print(xx.text)
    yy = calc(int(xx.text))
    print(1)
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(yy)

    print(2)
    input2 = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    input2.click()

    print(3)
    input3 = browser.find_element_by_xpath("//input[@id='robotsRule']")
    input3.click()



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()