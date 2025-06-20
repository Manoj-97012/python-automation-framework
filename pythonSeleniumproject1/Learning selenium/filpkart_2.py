from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element(By.XPATH,"//span[normalize-space()='Mobiles & Tablets']").click()
image = driver.find_element(By.XPATH, "//div[4]//div[1]//div[1]//a[1]//div[1]//img[2]")
driver.execute_script("arguments[0].scrollIntoView(true);", image)
image.click()

driver.find_element(By.XPATH,"//div[normalize-space()='Apple iPhone 16 Plus (Black, 128 GB)']").click()
window_handles = driver.window_handles

driver.switch_to.window(window_handles[1])
sleep(5)
driver.find_element(By.XPATH,"//button[@class='QqFHMw vslbG+ _3Yl67G _7Pd1Fp']").click()
driver.find_element(By.XPATH,"//button[@class='QqFHMw zA2EfJ _7Pd1Fp']").click()