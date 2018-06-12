from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Locators.locators import MacPageLocators

class MacPage():

    def __init__(self, driver):
        self.driver = driver
        self.locators = MacPageLocators
        self.wait = WebDriverWait(driver, 5)

    def open_buy_page_imac_pro(self):
        self.driver.find_element(*self.locators.imac_pro_buy).click()