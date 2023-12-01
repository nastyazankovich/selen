import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://suninjuly.github.io/math.html')
answer = driver.find_element(By.ID, 'answer')
x = 802
result = math.log(abs(12 * math.sin(x)))
checkbox = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
radiobutton = driver.find_element(By.CSS_SELECTOR, 'input[value="robots"]')
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

answer.send_keys(result)
checkbox.click()
radiobutton.click()
submit_button.click()
