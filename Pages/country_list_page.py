from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import CountryListPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from data.json_data import JsonActions


class CountryListPage():


    def __init__(self, driver):
        self.driver = driver
        self.locators = CountryListPageLocators
        self.wait = WebDriverWait(driver, 5)
        self.myjson = JsonActions()

    def checking_country_links(self):
        for link in self.driver.find_elements(*self.locators.select_country):
            ActionChains(self.driver).key_down(Keys.CONTROL) \
                .click(link) \
                .key_up(Keys.CONTROL) \
                .perform()
            self.driver.switch_to_window(self.driver.window_handles[1])
            jsonfile = self.myjson.read_json_file("countries_url_title_standart.json")
            assert jsonfile[self.driver.current_url[8:]] == self.driver.title
            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0])


    def test(self):
        dict = {}
        for link in self.driver.find_elements(*self.locators.select_country):
            ActionChains(self.driver).key_down(Keys.CONTROL) \
                .click(link) \
                .key_up(Keys.CONTROL) \
                .perform()
            self.driver.switch_to_window(self.driver.window_handles[1])
            dict[self.driver.current_url[8:]] = self.driver.title
            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0])
        self.myjson.write_json_file("countries_url_title_standart.json")
