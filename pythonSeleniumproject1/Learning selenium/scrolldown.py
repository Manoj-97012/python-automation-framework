from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

# scroll into view
driver.execute_script("window.scrollBy(0, 2000);")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels scrolled:", value)

# finding the perticar image in down
sleep(5)
flag=driver.find_element(By.XPATH,"//img[@alt='India']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
value_1 = driver.execute_script("return window.pageYOffset;")
print("Number of pixels scrolled:", value_1)

# scroll into down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
value_1 = driver.execute_script("return window.pageYOffset;")
print("Number of pixels scrolled:", value_1)
sleep(5)

driver.close()