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
driver.find_element(By.ID,"search-input").send_keys("software testing")
driver.find_element(By.ID,"search-button").click()
time.sleep(5)