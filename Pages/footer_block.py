from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import FooterLocators

class AllPagesCommonFooter():

    def __init__(self, driver):
        self.driver = driver
        self.locators = FooterLocators
        self.wait = WebDriverWait(driver, 5)

    def open_job_page(self):
        self.driver.find_element(*self.locators.job_at_apple_link).click()

    def open_country_list(self):
        self.driver.find_element(*self.locators.footer_country).click()
