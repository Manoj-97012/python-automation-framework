from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pythonSeleniumproject1.Python_Automation_projects.pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    login = LoginPage(driver)
    login.login("Admin", "admin123")
    # Wait for successful login (URL change or dashboard element)
    Successful_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
    )
    Dashboard_message = Successful_message.text
    assert "Dashboard" in Dashboard_message
    driver.quit()


