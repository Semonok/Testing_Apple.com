from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Locators.locators import CustomizeImacProPageLocators

class CustomizeImacProPage():

    def __init__(self, driver):
        self.driver = driver
        self.locators = CustomizeImacProPageLocators
        self.wait = WebDriverWait(driver, 5)

    def add_to_bag(self):
        self.driver.find_element(*self.locators.add_to_bag).click()