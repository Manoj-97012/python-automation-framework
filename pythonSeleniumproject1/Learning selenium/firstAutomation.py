import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://practice.expandtesting.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element("link text", "Test Cases").click()

