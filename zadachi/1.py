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
submit_button = driver.find_element(By.ID, "submit_button")
print(submit_button)
# time.sleep(2)
first_name_input.send_keys('Olga')
last_name_input.send_keys('Kaptiug')
city_input.send_keys('Vileyka')
country_input.send_keys('Belarus')
time.sleep(0.5)
submit_button.click()
time.sleep(1)
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(link)
#
# value1 = 'first_name'
# value2 = 'last_name'
# value3 = 'city'
# value4 = 'country'
#
# input1 = driver.find_element(By.TAG_NAME, value1)
# input1.send_keys("Ivan")
# input2 = driver.find_element(By.TAG_NAME, value2).send_keys("Petrov")
#
# input3 = driver.find_element(By.TAG_NAME, value3)
# input3.send_keys("Smolensk")
# time.sleep(2)
# input4 = driver.find_element(By.TAG_NAME, value4)
# input4.send_keys("Russia")
# button = driver.find_elements(By.CSS_SELECTOR, ".button.btn")
# time.sleep(2)
