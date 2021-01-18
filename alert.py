from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element_by_xpath("/html/body/form/div/div/button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num = browser.find_element_by_xpath("//*[@id='input_value']").text
    ans = math.log(abs(12 * math.sin(int(num))))

    input = browser.find_element_by_xpath("//*[@id='answer']")
    input.send_keys(str(ans))

    browser.find_element_by_xpath("/html/body/form/div/div/button").click()

finally:
    time.sleep(5)
    browser.quit()