from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Locators.locators import ImacProAccessoriesPageLocators

class ImacProAccessoriesPage():

    def __init__(self, driver):
        self.driver = driver
        self.locators = ImacProAccessoriesPageLocators
        self.wait = WebDriverWait(driver, 5)

    def review_bag(self):
        self.driver.find_element(*self.locators.review_bag).click()