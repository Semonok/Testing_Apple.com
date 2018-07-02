
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
    assert driver.bag_page.item_prices == driver.bag_page.subtotal_prices

def test_cheking_quantity_items_in_bag_10_and_opening_new_form(driver):
    driver.bag_page.choose_item_quantity('10+')
    assert driver.bag_page.quantity_field == "Input"

def test_cheking_invalid_quantity_in_bag(driver):
    driver.bag_page.choose_item_quantity(0)
    assert driver.bag_page.current_item_quantity != "0"
    driver.bag_page.choose_item_quantity(1000)
    assert driver.bag_page.current_item_quantity != "1000"

def test_checking_valid_quantity_in_input_field(driver):
    driver.bag_page.choose_item_quantity(11)
    assert driver.bag_page.current_item_quantity == "11"
    driver.bag_page.choose_item_quantity(999)
    assert driver.bag_page.current_item_quantity == "999"
    driver.bag_page.choose_item_quantity(1)
    assert driver.bag_page.current_item_quantity == "1"

def test_add_second_item(driver):
    driver.bag_page.add_second_item()
    assert driver.bag_page.summary_price(*driver.bag_page.items_prices) == driver.bag_page.subtotal_price

def test_delete_second_item(driver):
    count_items_before = len(driver.bag_page.items)
    driver.bag_page.remove_item()
    count_items_after = len(driver.bag_page.items)
    assert count_items_before == count_items_after + 1
    assert "iMac Pro" in driver.bag_page.items

def test_return_product_in_bag(driver):
    driver.bag_page.remove_item()
    assert driver.bag_page.notification_banner == "iMac Pro removed from your bag."
    driver.bag_page.return_product_in_bag()
    assert "iMac Pro" in driver.bag_page.items

def test_del_all_items_from_bag(driver):
    driver.bag_page.remove_item()
    assert driver.bag_page.main_text == "Your bag is empty."

def test_continue_shopping(driver):
    driver.bag_page.continue_shopping()
    assert driver.current_page('Home page') == True

def test_save_item_in_bag_for_signed_up_user(driver):
    driver.header_block.open_login_page()
    driver.login_page.sign_in(driver.login_data["correct_login"], driver.login_data["correct_password"])
    driver.login_page.success_login()
    driver.header_block.open_bag_page()
    if "iMac Pro" not in driver.bag_page.items:
        driver.header_block.open_mac_page()
        driver.mac_page.open_buy_page_imac_pro()
        driver.imac_pro_buy_page.open_customize_page()
        driver.customize_imac_pro_buy_page.add_to_bag()
        driver.imac_pro_accessories_page.review_bag()
        assert "iMac Pro" in driver.bag_page.items
        driver.header_block.sign_out()
        driver.header_block.open_login_page()
        driver.login_page.sign_in(driver.login_data["correct_login"], driver.login_data["correct_password"])
        driver.login_page.success_login()
        driver.header_block.open_bag_page()
    assert "iMac Pro" in driver.bag_page.items