from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://practice.expandtesting.com/")
driver.maximize_window()
#driver.execute_script("window.scrollTo(0, 200);")
# driver.find_element(By.XPATH,"Dynamic Table").click()
time.sleep(5)
element = driver.find_element(By.XPATH, "//a[text()='Dynamic Table']")
driver.execute_script("arguments[0].click();", element)
try:
    element=driver.find_element(By.XPATH,"//h1[text()='Dynamic Table page for Automation Testing Practice']")
    print("yes")
except:
    print("No")
driver.quit()