from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(5)
# one checkbox will select below code
driver.find_element(By.XPATH,value="//input[@id='sunday']").click()
#mutiple checkbox will select
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname == "sunday" or weekname == "monday":
#         checkbox.click()

#select last 2 checkbox
# sleep(5)
# for i in range (len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

# select first 4 checkbox
sleep(5)
for i in range (len(checkboxes)):
    if i < 5 :
        checkboxes[i].click()

# Checkbox notselected
sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


