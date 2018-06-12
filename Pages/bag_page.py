from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import BagPageLocators


class BagPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.locators = BagPageLocators

    @property
    def main_text(self):
        return self.driver.find_element(*self.locators.bag_main_text).text