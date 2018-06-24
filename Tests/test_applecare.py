def test_add_applecare_plus(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    driver.imac_pro_accessories_page.review_bag()
    assert "iMac Pro" in driver.bag_page.items
    driver.bag_page.add_applecare_plus()
    assert driver.bag_page.applecare_plus_price == "$169.00"
    assert driver.bag_page.summary_price(driver.bag_page.item_price, driver.bag_page.applecare_plus_price)\
           == driver.bag_page.subtotal_price


def test_remove_applecare_plus(driver):
    driver.bag_page.remove_applecare_plus()
    assert driver.bag_page.applecare_plus_price == None
    assert driver.bag_page.subtotal_price == driver.bag_page.item_price