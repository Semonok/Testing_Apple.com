from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import JobPageLocators
from selenium.webdriver.common.by import By


class JobPage():

    def __init__(self, driver):
        self.driver = driver
        self.locators = JobPageLocators
        self.wait = WebDriverWait(driver, 5)
        self.ActionChains = ActionChains(self.driver)

    def open_search_job_page(self):
        self.driver.find_element(*self.locators.open_search_job_page).click()
