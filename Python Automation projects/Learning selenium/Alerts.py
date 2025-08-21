from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
my_alert= driver.switch_to.alert.accept()
text_msg=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
text_msg = driver.switch_to.alert
#text_msg.accept()
text_msg.dismiss()
sleep(5)
