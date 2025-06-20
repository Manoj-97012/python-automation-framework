import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("9701240422")
input_field=driver.find_element(By.ID,"pass")
input_field.send_keys("Manoj@12345")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(5)