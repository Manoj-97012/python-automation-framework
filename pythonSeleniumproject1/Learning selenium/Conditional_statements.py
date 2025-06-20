from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
serachbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("display",serachbox.is_displayed())
print("display",serachbox.is_enabled())

is_man=driver.find_element(By.XPATH,"//input[@id='gender-male']")
is_man.click()
print(is_man.is_selected())