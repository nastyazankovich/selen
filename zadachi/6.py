import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.instagram.com/accounts/emailsignup/')
driver.execute_script("window.scrollBy(0, 100);")
number_input = driver.find_element(By.NAME, 'emailOrPhone')
full_name_input = driver.find_element(By.NAME, 'fullName')
name_input = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
number_input.send_keys('+375295429299')
full_name_input.send_keys('Olga12345987645678')
name_input.send_keys('Olga1234567765434567')
password.send_keys('12345678987654321')
submit_button.click()
