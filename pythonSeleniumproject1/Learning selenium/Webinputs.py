from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://practice.expandtesting.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Web inputs").click()
time.sleep(5)
driver.find_element(By.ID,"input-number").send_keys(1)
time.sleep(5)
input_field=driver.find_element(By.NAME,"input-text")
input_field.send_keys("Hello, Manoj!")
time.sleep(5)
date_field=driver.find_element(By.ID,"input-date")
date_field.send_keys("25-03-2025")
time.sleep(5)