from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from Loginpage.Ticketslogin import BuyTicket

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

Ticket = BuyTicket(driver)
Ticket.Ticket()

driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Akula")
driver.find_element(By.XPATH, "//input[@name='travlastname']").send_keys("Manojkumar")
driver.find_element(By.XPATH, "//input[@name='dob']").send_keys("18/09/1998")
radio = driver.find_element(By.XPATH, "//input[@id='sex_1']")
radio.click()
driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Bangalore")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Hyderabad")
sleep(2)
driver.find_element(By.XPATH, "//input[@id='departon']").send_keys("20/04/2025")
sleep(10)
visa_element = driver.find_element(By.XPATH, "//span[@id='select2-reasondummy-container']")
print("Text in element:", visa_element.text)
Email = driver.find_element(By.XPATH, "//input[@id='deliverymethod_1']")
Email.click()
driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("9701240422")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("akulamanojkumar454")
text = driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container' and @title='India']").text
print("Text in element:", text)
sleep(2)
text_1 = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span").text
print("Booking details :", text_1)
driver.close()
