from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 1500);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="card-body"]/h5[text()="Forms"]'))).click()
driver.find_element(By.XPATH,"(//div[@class='header-wrapper'])[2]").click()
sleep(10)
driver.find_element(By.XPATH,"(//li[@id='item-0'])[1]").click()
sleep(15)
