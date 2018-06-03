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
