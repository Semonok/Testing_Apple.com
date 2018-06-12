
def test_favorite_unsigning_up_user(driver):
    driver.header_block.open_favorites_page()
    assert driver.current_page == "LoginPage"