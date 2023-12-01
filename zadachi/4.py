import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://suninjuly.github.io/math.html')
num1 = driver.find_element(By.ID, 'num1').text
num2 = driver.find_element(By.ID, 'num2').text
sum = int(num2) + int(num1)
select = Select(driver.find_element(By.TAG_NAME, 'select'))
select.select_by_value(str(sum))
button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()
time.sleep(5)
driver.quit()
