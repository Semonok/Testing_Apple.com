from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import CheckOutPageLocators
from model import ConvertingPrice
from selenium.webdriver.common.action_chains import ActionChains
from data.json_data import JsonActions
from selenium.webdriver.common.keys import Keys

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.locators = CheckOutPageLocators
        self.convert = ConvertingPrice()
        self.myjson = JsonActions()

    def bad_button(self, locator):
        self.driver.execute_script("window.scrollTo(0, 0)")
        button_user = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(button_user).click().perform()

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
        self.bad_button(self.locators.delivery)

    def choose_pick_up(self):
        self.bad_button(self.locators.pick_up)

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

    def add_zip_code(self, zip):
        jsonfile = self.myjson.read_json_file("zip_codes.json")
        self.driver.find_element(*self.locators.enter_zip_code).clear()
        self.driver.find_element(*self.locators.enter_zip_code).send_keys(jsonfile[zip])
        self.bad_button(self.locators.zip_code_apply)

    def change_zip_code(self, zip):
        jsonfile = self.myjson.read_json_file("zip_codes.json")
        self.driver.find_element(*self.locators.zip_edit_button).click()
        self.wait.until(EC.element_to_be_clickable(self.locators.enter_zip_code))
        self.driver.find_element(*self.locators.enter_zip_code).clear()
        self.driver.find_element(*self.locators.enter_zip_code).send_keys(jsonfile[zip])
        self.bad_button(self.locators.zip_code_apply)

    def showing_zip_code(self, zip):
        jsonfile = self.myjson.read_json_file("zip_codes.json")
        try:
            self.wait.until(EC.text_to_be_present_in_element(self.locators.zip_edit_button, jsonfile[zip]))
            return True
        except:
            return False

    @property
    def wrong_zip_error_message(self):
        return self.driver.find_element(*self.locators.wrong_zip).text

    def summary_price(self, *price):
        result_price = 0
        for i in price:
            result_price += self.convert.convert_price_to_float(i)
        return self.convert.convert_float_to_price(result_price)

