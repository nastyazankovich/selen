import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://suninjuly.github.io/math.html')
answer = driver.find_element(By.ID, 'answer')
x = int(driver.find_element(By.ID, 'input_value').text)
result = math.log(abs(12 * math.sin(x)))
checkbox = driver.find_element(By.CLASS_NAME, 'form-check-label')
radiobutton = driver.find_element(By.ID, 'robotsRule')
submit_button = driver.find_element(By.CLASS_NAME, "btn.btn-default")
time.sleep(1)
answer.send_keys(str(result))
checkbox.click()
radiobutton.click()
time.sleep(0.5)
submit_button.click()
time.sleep(1)