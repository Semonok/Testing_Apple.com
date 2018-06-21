
def test_add_item_to_bag(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    assert "iMac Pro" in driver.header_block.items_in_bag
    driver.imac_pro_accessories_page.review_bag()
    assert "iMac Pro" in driver.bag_page.items
    assert driver.bag_page.item_price == driver.bag_page.total_price

def test_checking_quantity_items_in_bag_less_than_ten(driver):
    driver.bag_page.item_quantity_less_than_ten()
    assert driver.bag_page.item_prices == driver.bag_page.total_prices

def test_cheking_quantity_items_in_bag_10_and_opening_new_form(driver):
    driver.bag_page.choose_item_quantity("10+")
    assert driver.bag_page.quantity_field == "Input"

def test_cheking_invalid_quantity_in_bag(driver):
    driver.bag_page.choose_item_quantity(0)
    assert driver.bag_page.current_item_quantity != "0"
    driver.bag_page.choose_item_quantity(1000)
    assert driver.bag_page.current_item_quantity != "1000"

def test_checking_valid_quantity_in_input_field(driver):
    driver.bag_page.choose_item_quantity(1)
    assert driver.bag_page.current_item_quantity == "1"
    driver.bag_page.choose_item_quantity(11)
    assert driver.bag_page.current_item_quantity == "11"
    driver.bag_page.choose_item_quantity(999)
    assert driver.bag_page.current_item_quantity == "999"

def test_del_item_from_bag(driver):
    driver.bag_page.remove_item()
    assert driver.bag_page.main_text == "Your bag is empty."
