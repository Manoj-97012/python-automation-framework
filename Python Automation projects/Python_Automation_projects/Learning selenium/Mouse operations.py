from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://testautomationpractice.blogspot.com/")
# Mouse cover
point=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
sleep(5)
mobile=driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")

act=ActionChains(driver)
act.move_to_element(point).move_to_element(mobile).click().perform()

#Double click element
input=driver.find_element(By.XPATH,"//input[@id='field1']")
input.clear()
input.send_keys("Welcome")

button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act=ActionChains(driver)
act.double_click(button).click().perform()
sleep(5)

#drag and drop
act=ActionChains(driver)
first=driver.find_element(By.XPATH,"//div[@id='draggable']")
second=driver.find_element(By.XPATH,"//div[@id='droppable']")

act.drag_and_drop(first,second).perform()

# drag and drop by offset
act=ActionChains(driver)
max=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
min=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")
sleep(10)
print("Location of silder.berfore siding:")
print(max.location)
print(min.location)
act.drag_and_drop_by_offset(max,100,0).perform()
act.drag_and_drop_by_offset(min,39,0).perform()

# scroll down by pixel
sleep(5)
driver.execute_script("window.scrollBy(0, 3000);")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels scrolled:", value)



