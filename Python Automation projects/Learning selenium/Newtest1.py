import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://trytestingthis.netlify.app/")
driver.maximize_window()

print("Page Title:", driver.title)
time.sleep(10)
input_text_1 = driver.find_element(By.ID,'fname')
input_text_1.send_keys('Manoj')

input_text_2 = driver.find_element(By.ID,'lname')
input_text_2.send_keys('Kumar')


radio = driver.find_element(By.ID,"male")
radio.is_selected()
if radio:
    print("Option 1 is selected.")
else:
    print("Option 1 is NOT selected.")
driver.implicitly_wait(5)

option = driver.find_element(By.NAME,"option")
option.select_by_visible_text('option 1')
time.sleep(10)

#is_selected = driver.find_element(By.XPATH,'//input[@name="option1"]').is_selected()
