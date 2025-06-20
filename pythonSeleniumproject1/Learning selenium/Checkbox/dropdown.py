from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
select_element=driver.find_element(By.XPATH,"//select[@id='country']")
dropdown=Select(select_element)
sleep(5)
dropdown.select_by_visible_text("India")
sleep(5)
dropdown.select_by_index(3)
sleep(5)
alloptions=dropdown.options
print("number of dropdown :", len(alloptions))

for i in alloptions:
    if i.text == "Germany":
        print(i.text)
        break

driver.quit()


