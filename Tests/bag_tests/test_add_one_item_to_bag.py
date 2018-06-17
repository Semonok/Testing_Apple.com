
def test_add_item_to_bag(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    assert "iMac Pro" in driver.header_block.items_in_bag
    driver.imac_pro_accessories_page.review_bag()
    assert "iMac Pro" in driver.bag_page.items
    assert driver.bag_page.item_price == driver.bag_page.total_price