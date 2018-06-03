
def test_confirm_region(driver):
    driver.common_header.accept_country("ru")
    assert driver.page_title == "Apple (Россия) – Официальный сайт"