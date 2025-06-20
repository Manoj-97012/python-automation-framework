from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# for element in elements:
#     print(element.text)
#     print(len(element.text))

# element_exception=driver.find_element(By.LINK_TEXT,"Log")
# element_exception.click()

element_exception=driver.find_element(By.LINK_TEXT,"Log")
print(len(element_exception))
