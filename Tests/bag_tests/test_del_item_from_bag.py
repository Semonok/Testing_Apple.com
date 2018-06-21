
def test_del_item_to_bag(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    driver.imac_pro_accessories_page.review_bag()
    driver.bag_page.remove_item()
    assert driver.bag_page.main_text == "Your bag is empty."