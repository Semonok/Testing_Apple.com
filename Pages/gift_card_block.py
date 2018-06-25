from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import GiftCardBlockLocators

class GiftCardBlock:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,3)
        self.locators = GiftCardBlockLocators

    def write_message(self,message=""):
        self.driver.find_element(*self.locators.gift_message).click()
        self.wait.until(EC.presence_of_element_located(self.locators.gift_message_text))
        self.driver.find_element(*self.locators.gift_message_text).clear()
        self.driver.find_element(*self.locators.gift_message_text).send_keys(message)

    def save_changes(self):
        self.driver.find_element(*self.locators.gift_save_button).click()

    def cancel_gift_card_menu(self):
        self.driver.find_element(*self.locators.gift_cancel_button).click()

    def remove_message(self):
        self.driver.find_element(*self.locators.gift_none).click()
        self.save_changes()

    @property
    def alert(self):
        return self.driver.find_element(*self.locators.gift_error_message).text