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

    @property
    def favorites_items(self):
        a=[]
        for i in self.driver.find_elements(*self.locators.item_name):
            a.append(i.text)
        return a

    def remove_item(self, item):
        self.driver.find_element(*self.locators.edit_remove).click()
        i = 0
        while i < len(self.favorites_items):
            element = self.driver.find_element(*self.locators.item_name)
            i+=1
            if element.text == item:
                element.find_element(*self.locators.select_item_relative_by_edit_name).click()
            self.driver.find_element(*self.locators.edit_remove).click()