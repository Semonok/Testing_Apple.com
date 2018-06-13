from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
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

    @property
    def favorites_count_in_settings_menu(self):
        self.open_settings_menu()
        return int(self.driver.find_element(*self.locators.favotites_page).text[11:-1])

    def open_bag_page(self):
        self.open_settings_menu()
        self.driver.find_element(*self.locators.bag_page).click()

    def open_search(self):
        self.driver.find_element(*self.locators.search_menu).click()

    @property
    def five_quick_links_are_present(self):
        if len(self.driver.find_elements(*self.locators.quick_link)) == 5:
            return True
        else:
            return False

    def search_item(self,item):
        self.driver.find_element(*self.locators.search_field).clear()
        self.driver.find_element(*self.locators.search_field).send_keys(item)
        self.driver.find_element(*self.locators.search_field).send_keys(Keys.ENTER)

    def open_iphone_page(self):
        self.driver.find_element(*self.locators.iphone_page).click()

    def open_mac_page(self):
        self.driver.find_element(*self.locators.mac_page).click()

