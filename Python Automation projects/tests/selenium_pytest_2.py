import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Fixture to launch and quit browser
@pytest.fixture()
def driver():
    service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Test with multiple sets of credentials
@pytest.mark.parametrize("username, password", [
    ("test", "test"),
    ("user2", "pass2"),
    ("user3", "pass3"),
])
def test_flipkart_login(driver, username, password):
    driver.get("https://trytestingthis.netlify.app/")
    time.sleep(2)
    driver.implicitly_wait(5)

    # Enter username and password
    driver.find_element(By.ID, "uname").send_keys(username)
    driver.find_element(By.ID, "pwd").send_keys(password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Assert login result
    assert "Login Successful" in driver.page_source or "Successful" in driver.page_source
