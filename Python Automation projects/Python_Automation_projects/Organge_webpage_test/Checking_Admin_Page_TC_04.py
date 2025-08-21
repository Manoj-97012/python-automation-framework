from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pythonSeleniumproject1.Python_Automation_projects.pages.login_page import LoginPage


def test_Admin_Icon_page():
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()


        login = LoginPage(driver)
        login.login("Admin", "admin123")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]")).click()