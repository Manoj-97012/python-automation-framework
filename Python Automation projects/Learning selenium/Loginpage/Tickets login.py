import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By


class BuyTicket:
    def __init__(self,driver):
        self.driver = driver
        self.BuyTicketLink = (By.LINK_TEXT, "Buy Ticket")
        self.checkbox = (By.XPATH, "//input[@id='product_549']")



    def Ticket(self):
        self.driver.find_element(*self.BuyTicketLink).click()
        self.driver.find_element(*self.checkbox).click()