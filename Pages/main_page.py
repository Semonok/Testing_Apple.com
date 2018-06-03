from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Locators.locators import MainPageLocators, HeaderLocators, FooterLocators

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_mac_page(self):
        self.driver.find_element(HeaderLocators)

    @property
    def ipad_page(self):
        return self.driver.find_element(By.XPATH, Locators.ipad_page)

    @property
    def iphone_page(self):
        return self.driver.find_element(By.XPATH, Locators.iphone_page)

    @property
    def watch_page(self):
        return self.driver.find_element(By.XPATH, Locators.watch_page)

    @property
    def tv_page(self):
        return self.driver.find_element(By.XPATH, Locators.appletv_page)

    @property
    def music_page(self):
        return self.driver.find_element(By.XPATH, Locators.music_page)

    @property
    def support_page(self):
        return self.driver.find_element(By.XPATH, Locators.support_page)

    @property
    def bag_menu(self):
        return self.driver.find_element(By.XPATH, Locators.bag)

    @property
    def search_menu(self):
        return self.driver.find_element(By.XPATH, Locators.search_open)

    @property
    def country_selection_menu(self):
        return self.driver.find_element(By.XPATH, Locators.country_selection_menu)

    @property
    def choose_country(self):
        return self.driver.find_element(By.XPATH, Locators.choose_country)

    @property
    def accept_region(self):
        return self.driver.find_element(By.XPATH, Locators.accept_region)
