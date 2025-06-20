from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Open New Window").click()
windows = driver.window_handles

# Switch to the new window
driver.switch_to.window(windows[1])

# Do something in the new window
print(driver.title)

# Switch back to the original window
driver.switch_to.window(windows[0])