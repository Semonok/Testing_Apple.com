
def test_sign_in_empty_password(driver):
    driver.header_block.open_login_page()
    driver.login_page.sign_in('semonok95@gmail.com','')
    assert driver.login_page.password_error() == "Password is missing."

def test_sign_in_empty_login(driver):
    driver.login_page.sign_in('','123456')
    assert driver.login_page.login_error() == "Apple ID is missing."

def test_sign_in_empty_all_fields(driver):
    driver.login_page.sign_in('','')
    assert driver.login_page.login_error() == "Apple ID is missing."
    assert driver.login_page.password_error() == "Password is missing."

def test_sign_in_invalid_login_or_password(driver):
    driver.login_page.sign_in('semonok95@gmail.com','123456')
    assert driver.login_page.sign_in_error() == "Your AppleConnect account or password was entered incorrectly."

def test_sign_in_valid_login_and_password(driver):
    driver.login_page.sign_in('semonok95@gmail.com','********')
    assert driver.url_changes_to("https://www.apple.co/") == True
    assert driver.header_block.which_user_sign_in() == "Семён"
    driver.header_block.sign_out()