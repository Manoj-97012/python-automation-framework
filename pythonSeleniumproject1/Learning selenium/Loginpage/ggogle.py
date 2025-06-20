from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.se/?hl=sv")

text=driver.title
print(text)

assert "Google" in text









