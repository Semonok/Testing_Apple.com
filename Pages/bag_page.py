from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import BagPageLocators
from Locators.locators import GiftCardBlockLocators
from selenium.webdriver.support.ui import Select
from model import ConvertingPrice
from selenium.webdriver.common.keys import Keys
from data.json_data import JsonActions
import time

class BagPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.locators = BagPageLocators
        self.gift_locators = GiftCardBlockLocators
        self.myjson = JsonActions()
        self.convert = ConvertingPrice()
        self.item_prices = []
        self.subtotal_prices = []

    @property
    def main_text(self):
        self.wait.until(EC.presence_of_element_located(self.locators.continue_shopping))
        return self.driver.find_element(*self.locators.bag_main_text).text

    @property
    def items(self):
        item_list = []
        for item in self.driver.find_elements(*self.locators.items_name):
            item_list.append(item.text)
        return item_list

    @property
    def quantity(self):
        try:
            return self.driver.find_element(*self.locators.quantity_less_ten).get_attribute("value")
        except:
            return self.driver.find_element(*self.locators.quantity_more_ten).get_attribute("value")

    def remove_item(self):
        self.driver.find_element(*self.locators.remove).click()

    @property
    def item_price(self):
        return self.driver.find_element(*self.locators.item_price).text

    @property
    def subtotal_price(self):
        return self.driver.find_element(*self.locators.subtotal_price).text

    @property
    def tax_price(self):
        price = self.driver.find_element(*self.locators.summary_tax_value).text
        if price == "$ –":
            return None
        else:
            return price

    @property
    def total_price(self):
        return self.driver.find_element(*self.locators.total_price).text

    def summary_price(self, *price):
        result_price = 0
        for i in price:
            result_price +=self.convert.convert_price_to_float(i)
        return self.convert.convert_float_to_price(result_price)


    def item_quantity_less_than_ten(self):
        select = Select(self.driver.find_element(*self.locators.quantity_less_ten))
        one_item_price = self.item_price
        for i in range(1,10):
            select.select_by_value(str(i))
            self.wait.until(EC.text_to_be_present_in_element
                            (self.locators.item_price,self.convert.converting_price(one_item_price,i)))
            self.item_prices.append(self.item_price)
            self.subtotal_prices.append(self.subtotal_price)

    @property
    def current_item_quantity(self):
        try:
            return self.driver.find_element(*self.locators.quantity_less_ten).get_attribute("value")
        except:
            return self.driver.find_element(*self.locators.quantity_more_ten).get_attribute("value")

    def choose_item_quantity(self,quantity):
        if len(self.driver.find_elements(*self.locators.quantity_more_ten)) == 0:
            if quantity in range(1,10) or quantity is '10+':
                Select(self.driver.find_element(*self.locators.quantity_less_ten)).select_by_value(str(quantity))
            else:
                Select(self.driver.find_element(*self.locators.quantity_less_ten)).select_by_value("10+")
                self.driver.find_element(*self.locators.quantity_more_ten).clear()
                self.driver.find_element(*self.locators.quantity_more_ten).send_keys(quantity)
                self.driver.find_element(*self.locators.quantity_more_ten).send_keys(Keys.ENTER)
        else:
            self.driver.find_element(*self.locators.quantity_more_ten).click()
            self.driver.find_element(*self.locators.quantity_more_ten).clear()
            self.driver.find_element(*self.locators.quantity_more_ten).send_keys(quantity)
            self.driver.find_element(*self.locators.quantity_more_ten).send_keys(Keys.ENTER)


    @property
    def quantity_field(self):
        if len(self.driver.find_elements(*self.locators.quantity_more_ten)) != 0:
            return "Input"
        else:
            return "Select"

    def enter_zip_code(self,zip):
        jsonfile = self.myjson.read_json_file("zip_codes.json")
        self.driver.find_element(*self.locators.enter_zip_code).click()
        self.driver.find_element(*self.locators.zip_code_field).clear()
        self.driver.find_element(*self.locators.zip_code_field).send_keys(jsonfile[zip])
        self.driver.find_element(*self.locators.zip_code_apply).click()
        price = self.driver.find_element(*self.locators.summary_tax_value).text
        if len(self.driver.find_elements(*self.locators.zip_code_apply)) == 0:
            self.wait.until_not(EC.text_to_be_present_in_element(self.locators.summary_tax_value, price))

    @property
    def zip_code_error(self):
        self.wait.until(EC.presence_of_element_located(self.locators.zip_code_error))
        return self.driver.find_element(*self.locators.zip_code_error).text

    def cancel_zip_code(self):
        self.driver.find_element(*self.locators.zip_code_cancel).click()

    def add_applecare_plus(self):
        self.driver.find_element(*self.locators.applecare_plus_add).click()
        self.wait.until(EC.presence_of_element_located(self.locators.applecare_plus_remove))

    def remove_applecare_plus(self):
        self.driver.find_element(*self.locators.applecare_plus_remove).click()
        self.wait.until(EC.presence_of_element_located(self.locators.applecare_plus_add))

    @property
    def applecare_plus_price(self):
        if len(self.driver.find_elements(*self.locators.applecare_plus_price)) == 0:
            return None
        else:
            return self.driver.find_element(*self.locators.applecare_plus_price).text

    def open_gift_card(self):
        self.driver.find_element(*self.locators.gift_message_add).click()

    def edit_gift_card(self):
        self.driver.find_element(*self.locators.gift_message_edit).click()

    @property
    def gift_message_text(self):
        self.wait.until(EC.invisibility_of_element_located(self.gift_locators.gift_header))
        try:
            return self.driver.find_element(*self.locators.gift_message_text).text
        except:
            return None

    @property
    def alert_message(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.locators.alert_message))
            return self.driver.find_element(*self.locators.alert_message).text
        except:
            return "Alert message is not presence"

    @property
    def alert_message_is_not_presence(self):
        try:
            self.wait.until_not(EC.presence_of_element_located(self.locators.alert_message))
            return True
        except:
            return "Alert message is not presence:", self.driver.find_element(*self.locators.alert_message).text





