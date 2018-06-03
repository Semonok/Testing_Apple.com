
def test_confirm_region(driver):
    driver.header_block.accept_country("ru")
    assert driver.page_title == "Apple (Россия) – Официальный сайт"