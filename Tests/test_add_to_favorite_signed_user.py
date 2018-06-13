
def test_add_to_favorite_signed_user(driver):
    driver.header_block.open_login_page()
    driver.login_page.sign_in(driver.login_data["correct_login"], driver.login_data["correct_password"])
    driver.login_page.success_login()
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.add_to_favorites()
    driver.header_block.open_favorites_page()
    assert "iMac Pro" in driver.favorites_page.favorites_items