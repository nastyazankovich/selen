import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://suninjuly.github.io/simple_form_find_task.html')
first_name_input = driver.find_element(By.NAME, 'first_name')
last_name_input = driver.find_element(By.NAME, 'last_name')
city_input = driver.find_element(By.NAME, 'firstname')
country_input = driver.find_element(By.ID, 'country')
submit_button = driver.find_element(By.CSS_SELECTOR, 'form button[type=submit]')
first_name_input.send_keys('Olga')
last_name_input.send_keys('Kaptiug')
city_input.send_keys('Vileyka')
country_input.send_keys('Belarus')
submit_button.click()