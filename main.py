from selenium import webdriver
import time
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

while True:
    cookie.click()
    if time.time() > timeout:
        timeout += 10
