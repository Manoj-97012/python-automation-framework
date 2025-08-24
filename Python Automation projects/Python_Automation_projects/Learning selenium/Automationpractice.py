from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

input_text=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
input_text.send_keys("Selenium")
sleep(2)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
sleep(2)
print("The title :", driver.title)
