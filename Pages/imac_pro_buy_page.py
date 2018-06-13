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
        self.driver.find_element(*self.locators.favorites_button).click()
