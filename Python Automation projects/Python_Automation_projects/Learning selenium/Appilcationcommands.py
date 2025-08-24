from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://practice.expandtesting.com/")
print(driver.title)#Practice Test Automation WebSite
print(driver.current_url)#https://practice.expandtesting.com/
print(driver.page_source)

driver.quit()