from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import CheckOutPageLocators
from model import ConvertingPrice
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.locators = CheckOutPageLocators
        self.convert = ConvertingPrice()

    @property
    def total_price(self):
        return self.driver.find_element(*self.locators.summary_price).text

    def show_order_summary(self):
        self.driver.find_element(*self.locators.show_order_summary).click()
        self.wait.until(EC.visibility_of_element_located(self.locators.order_menu_header))

    @property
    def order_menu_total_price(self):
        return self.driver.find_element(*self.locators.order_menu_total_price).text

    @property
    def order_menu_header(self):
        return self.driver.find_element(*self.locators.order_menu_header).text

    def edit_bag(self):
        self.driver.find_element(*self.locators.edit_bag).click()

    @property
    def secure_message(self):
        return self.driver.find_element(*self.locators.secure_message).text

    def continue_to_bag(self):
        self.driver.find_element(*self.locators.secure_message_continue).click()

    def close_order_menu(self):
        self.driver.find_element(*self.locators.close_order_menu).click()

    def choose_delivery(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        button_user = self.driver.find_element(*self.locators.delivery)
        ActionChains(self.driver).move_to_element(button_user).click().perform()

    def choose_pick_up(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        button_user = self.driver.find_element(*self.locators.pick_up)
        ActionChains(self.driver).move_to_element(button_user).click().perform()

    @property
    def delivery_header(self):
        hidden = self.driver.find_element(*self.locators.hidden_header).text
        return self.driver.find_element(*self.locators.delivery_header).text.replace('\n'+hidden, "")

    @property
    def pick_up_header(self):
        return self.driver.find_element(*self.locators.pick_up_header).text

    @property
    def delivery_product(self):
        return self.driver.find_element(*self.locators.delivery_product).text

    def delivery_tommorow(self):
        self.driver.find_element(*self.locators.delivery_tommorow).click()
        self.wait.until_not(EC.text_to_be_present_in_element(self.locators.summary_price, self.total_price))

    @property
    def delivery_tommorow_price(self):
        return self.driver.find_element(*self.locators.delivery_tommorow_price).text

    @property
    def pick_up_zip_message(self):
        return self.driver.find_element(*self.locators.pick_up_zip_message).text

    def summary_price(self, *price):
        result_price = 0
        for i in price:
            result_price += self.convert.convert_price_to_float(i)
        return self.convert.convert_float_to_price(result_price)

