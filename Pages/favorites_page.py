from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import FavoritesPageLocators
class FavoritesPage():

    def __init__(self, driver):
        self.driver = driver
        self.locators = FavoritesPageLocators
        self.wait = WebDriverWait(driver, 5)

    @property
    def favorites_text_that_list_is_empty(self):
        return self.driver.find_element(*self.locators.empty_list).text