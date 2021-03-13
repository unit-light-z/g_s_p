from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "https://suninjuly.github.io/execute_script.html"
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
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()

    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # # assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"

    # Отправляем заполненную форму

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()