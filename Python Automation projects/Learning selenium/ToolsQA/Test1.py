from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/")
driver.maximize_window()

title_1= driver.title
print(title_1)

assert "DEMOQA" == title_1
