from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Computers").click()
driver.find_element(By.LINK_TEXT,"Desktops").click()
button=driver.find_element(By.CLASS_NAME,"button-2 product-box-add-to-cart-button")
button.click()
print("button clicked")
sleep(10)

driver.quit()