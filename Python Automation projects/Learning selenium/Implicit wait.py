from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
driver.implicitly_wait(10)
checkbox= driver.find_element(By.XPATH, "//input[@value='M']")
checkbox.click()
if checkbox.is_selected():
    print("checkbox is clicked")
else:
    print("checkbox not clicked")
input_field=driver.find_element(By.XPATH,"//input[@id='FirstName']")
input_field.send_keys("Akula")
input_field=driver.find_element(By.XPATH,"//input[@id='LastName']")
input_field.send_keys("Manojkumar")

driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Manoj@12345")
driver.implicitly_wait(10)
sleep(15)
driver.quit()