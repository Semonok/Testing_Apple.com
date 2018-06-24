
def test_checking_quantity_items_in_bag_less_than_ten(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    driver.imac_pro_accessories_page.review_bag()
    assert "iMac Pro" in driver.bag_page.items
    driver.bag_page.item_quantity_less_than_ten()
    assert driver.bag_page.item_prices == driver.bag_page.subtotal_prices