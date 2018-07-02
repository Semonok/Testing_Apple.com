
def test_check_out_unsigned_user(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    driver.imac_pro_accessories_page.review_bag()
    assert "iMac Pro" in driver.bag_page.items
    driver.bag_page.check_out()
    assert driver.current_page("Login page") == True

def test_check_out_page(driver):
    driver.login_page.guest_login()
    assert driver.current_page("Check out page") == True
    assert driver.check_out_page.delivery_header == "In stock and ready to ship."
    assert driver.check_out_page.delivery_product == "iMac Pro"

def test_delivery_tommorow_option(driver):
    price_before = driver.check_out_page.total_price
    delivery_price = driver.check_out_page.delivery_tommorow_price
    driver.check_out_page.delivery_tommorow()
    price_after = driver.check_out_page.total_price
    assert driver.check_out_page.summary_price(price_before,delivery_price) == price_after

def test_checking_pick_up(driver):
    driver.check_out_page.choose_pick_up()
    assert driver.check_out_page.pick_up_zip_message == 'Enter a zip code to see item availability for nearby stores.'

def test_order_info(driver):
    driver.check_out_page.show_order_summary()
    assert driver.check_out_page.total_price == driver.check_out_page.order_menu_total_price
    assert driver.check_out_page.order_menu_header == "Your Order Total"

def test_edit_page(driver):
    driver.check_out_page.edit_bag()
    assert driver.check_out_page.secure_message == "Leaving Secure Checkout"
    driver.check_out_page.continue_to_bag()
    assert driver.current_page("Bag page") == True