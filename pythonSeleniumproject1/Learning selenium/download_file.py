from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Download Files']").click()
enter=driver.find_element(By.XPATH,"//textarea[@id='inputText']")
enter.send_keys("Manoj is good boy")

driver.find_element(By.XPATH,"//button[@id='generateTxt']").click()
driver.find_element(By.XPATH,"//a[@id='txtDownloadLink']").click()

driver.close()
