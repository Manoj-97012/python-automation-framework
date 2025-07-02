from selenium import webdriver
from pythonSeleniumproject1.Python_Automation_projects.pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    login = LoginPage(driver)
    login.login("Admin", "admin123")
    # Wait for successful login (URL change or dashboard element)
    assert "dashboard" in driver.current_url.lower() or "dashboard" in driver.page_source.lower()

    driver.quit()


