from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import LoginPageLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)


    def sign_in(self, username, password):
        self.driver.find_element(*LoginPageLocators.login).clear()
        self.driver.find_element(*LoginPageLocators.login).send_keys(username)
        self.driver.find_element(*LoginPageLocators.password).clear()
        self.driver.find_element(*LoginPageLocators.password).send_keys(password)
        self.driver.find_element(*LoginPageLocators.confirm_button).click()

    def guest_login(self):
        self.driver.find_element(*LoginPageLocators.guest_checkout).click()

    def success_login(self):
        self.wait.until(EC.url_to_be("https://www.apple.com/"))

    def login_error(self):
        return self.driver.find_element(*LoginPageLocators.login_error).text

    def password_error(self):
        return self.driver.find_element(*LoginPageLocators.password_error).text

    def sign_in_error(self):
        return self.driver.find_element(*LoginPageLocators.main_error).text
