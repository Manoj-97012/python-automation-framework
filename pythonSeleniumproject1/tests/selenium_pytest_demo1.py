import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def driver():
    service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_filpkart(driver):

    # driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(4)
    # driver.find_element(By.XPATH,"//div[@class='H6-NpN _3N4_BX']").click()
    # sleep(2)
    # email=driver.find_element(By.XPATH,"//input[@class='r4vIwl mYpCuj BV+Dqf']")
    # email.send_keys("akulamanojkumar454@gmail.com")
    try:
        close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_button.click()
    except:
        print("Login popup not found or already closed.")

    text = driver.find_element(By.NAME, "q")
    text.send_keys("Laptops")
    text.send_keys(Keys.RETURN)
