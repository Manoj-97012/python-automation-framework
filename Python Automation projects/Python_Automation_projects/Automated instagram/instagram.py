from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    #username= driver.find_element(By.XPATH,'//input[@name="username"]')
    username.send_keys('manoj_k_umar_royal')
    password=wait.until(EC.presence_of_element_located((By.NAME,"password")))
    password.send_keys('Manoj@12345')
    submit = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@type="submit"]')))
    submit.click()
    search_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[name()="svg" and @aria-label="Search"]')
    ))
    search_icon.click()
    input_1 = wait.until(EC.presence_of_element_located(
        (By.XPATH, '(//input[contains(@placeholder,"Search")])[1]')
    ))
    input_1.send_keys("charan_ck06")
    select_id = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '(//span[normalize-space()="charan_ck06"])[2]')
    ))
    select_id.click()