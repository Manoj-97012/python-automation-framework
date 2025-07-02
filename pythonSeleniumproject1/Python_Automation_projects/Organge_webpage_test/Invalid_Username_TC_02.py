from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pythonSeleniumproject1.Python_Automation_projects.pages.login_page import LoginPage

def test_Invalid_username():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    login = LoginPage(driver)
    login.login("Manoj", "admin123")
    error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))
    )
    invalid_username_text = error_element.text
    print("Captured Error Message:", invalid_username_text)

    assert "Invalid credentials" in invalid_username_text
    driver.quit()