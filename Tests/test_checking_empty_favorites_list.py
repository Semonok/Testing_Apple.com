
def test_checking_empty_favourites_list(driver):
    driver.header_block.open_login_page()
    driver.login_page.sign_in(driver.login_data["correct_login"], driver.login_data["correct_password"])
    driver.login_page.success_login()
    driver.header_block.open_favorites_page()
    assert driver.favorites_page.favorites_text_that_list_is_empty == "You don’t have any Favorites."
