
def test_save_item_in_bag_for_signed_up_user(driver):
    driver.header_block.open_login_page()
    driver.login_page.sign_in(driver.login_data["correct_login"], driver.login_data["correct_password"])
    driver.login_page.success_login()
    if "iMac Pro" not in driver.header_block.items_in_bag:
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
