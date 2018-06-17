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
        self.wait.until(EC.presence_of_element_located(self.locators.continue_shopping))
        return self.driver.find_element(*self.locators.bag_main_text).text

    @property
    def items(self):
        item_list = []
        for item in self.driver.find_elements(*self.locators.items_name):
            item_list.append(item.text)
        return item_list

    def remove_item(self):
        self.driver.find_element(*self.locators.remove).click()

    @property
    def item_price(self):
        return self.driver.find_element(*self.locators.item_price).text

    @property
    def total_price(self):
        return self.driver.find_element(*self.locators.total_price).text