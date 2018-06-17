from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Locators.locators import ImacProBuyPageLocators

class ImacProBuyPage():

    def __init__(self, driver):
        self.driver = driver
        self.locators = ImacProBuyPageLocators
        self.wait = WebDriverWait(driver, 5)

    def add_to_favorites(self):
        if len(self.driver.find_elements(*self.locators.remove_favorites_button)) == 1:
            self.driver.find_element(*self.locators.remove_favorites_button).click()
        self.driver.find_element(*self.locators.add_favorites_button).click()

    def open_customize_page(self):
        self.driver.find_element(*self.locators.configure).click()
