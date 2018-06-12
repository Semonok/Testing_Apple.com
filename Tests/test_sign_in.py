
def test_sign_in_empty_password(driver):
    driver.header_block.open_login_page()
    driver.login_page.sign_in(driver.login_data["correct_login"],driver.login_data["empty_password"])
    assert driver.login_page.password_error() == "Password is missing."

def test_sign_in_empty_login(driver):
    driver.login_page.sign_in(driver.login_data["empty_login"],driver.login_data["correct_login"])
    assert driver.login_page.login_error() == "Apple ID is missing."

def test_sign_in_empty_all_fields(driver):
    driver.login_page.sign_in(driver.login_data["empty_login"],driver.login_data["empty_password"])
    assert driver.login_page.login_error() == "Apple ID is missing."
    assert driver.login_page.password_error() == "Password is missing."

def test_sign_in_invalid_password(driver):
    driver.login_page.sign_in(driver.login_data["correct_login"],driver.login_data["incorrect_password"])
    assert driver.login_page.sign_in_error() == "Your AppleConnect account or password was entered incorrectly."

def test_sign_in_valid_login_and_password(driver):
    driver.login_page.sign_in(driver.login_data["correct_login"],driver.login_data["correct_password"])
    driver.login_page.success_login()
    assert driver.header_block.which_user_sign_in() == "Test"
    driver.header_block.sign_out()