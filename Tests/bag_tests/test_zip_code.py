def test_invalid_zip_code(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    driver.imac_pro_accessories_page.review_bag()
    assert "iMac Pro" in driver.bag_page.items
    driver.bag_page.enter_zip_code("Invalid")
    assert driver.bag_page.zip_code_error == "Please enter a valid zip code."
    assert driver.bag_page.tax_price is None
    driver.bag_page.cancel_zip_code()

def test_valid_zip_code(driver):
    driver.bag_page.enter_zip_code("Valid")
    assert driver.bag_page.tax_price is not None
    assert driver.bag_page.summary_price(driver.bag_page.tax_price, driver.bag_page.subtotal_price)\
           == driver.bag_page.total_price