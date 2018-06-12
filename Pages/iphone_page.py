from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Locators.locators import IphonePageLocators

class IphonePage():

    def __init__(self, driver):
        self.driver = driver
        self.locators = IphonePageLocators
        self.wait = WebDriverWait(driver, 5)

    def open_accessories(self):
        self.driver.find_element(*self.locators.accessories).click()