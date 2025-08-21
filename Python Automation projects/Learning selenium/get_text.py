from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

# email_send=driver.find_element(By.XPATH,"//input[@id='Email']")
#
# email_send.clear()
# email_send.send_keys("akulamanoj")
#
# print("result of text:",email_send.text)
# print("result of attribute:",email_send.get_attribute("value"))

Login=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")

print("result of text:",Login.text)
print("result of attribute:",Login.get_attribute("value"))
print("result of attribute:",Login.get_attribute("type"))