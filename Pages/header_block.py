from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import HeaderLocators

class AllPagesCommonHeader():

    def __init__(self, driver):
        self.driver = driver
        self.locators = HeaderLocators
        self.wait = WebDriverWait(driver, 5)

    def accept_country(self, country_prefix):
        self.driver.find_element(*self.locators.accept_region).click()
        self.wait.until(EC.url_to_be("https://www.apple.com/"+country_prefix+"/"))

    def open_settings_menu(self):
        self.driver.find_element(*self.locators.settings_menu).click()

    def sign_out(self):
        self.open_settings_menu()
        try:
            self.driver.find_element(*self.locators.sign_out).click()
        except:
            pass

    def open_login_page(self):
        self.open_settings_menu()
        try:
            self.driver.find_element(*self.locators.sign_in_page).click()
        except:
            self.driver.find_element(*self.locators.sign_out).click()
            self.open_settings_menu()
            self.driver.find_element(*self.locators.sign_in_page).click()

    def which_user_sign_in(self):
        self.open_settings_menu()
        return self.driver.find_element(*self.locators.sign_out).text[9:]

    def open_favorites_page(self):
        self.open_settings_menu()
        self.driver.find_element(*self.locators.favotites_page).click()

    def open_bag_page(self):
        self.open_settings_menu()
        self.driver.find_element(*self.locators.bag_page).click()