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

@pytest.mark.parametrize("username, password", [
    ("test", "test"),
    ("user2", "pass2"),
    ("user3", "pass3"),
])

def test_filpkart(driver, username_field, password_field, submit_button, ):
    driver.get("https://trytestingthis.netlify.app/")
    time.sleep(5)
    driver.implicitly_wait(5)
    driver.find_element(By.ID,"uname").send_keys("test")
    driver.find_element(By.ID,"pwd").send_keys("test")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    assert "Successful" in driver.page_source