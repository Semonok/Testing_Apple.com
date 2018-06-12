
def test_add_to_favorite(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.add_to_favorites()
    assert driver.current_page("Login page") == True
