
def test_bag_page_is_empty(driver):
    driver.header_block.open_bag_page()
    assert driver.bag_page.main_text == "Your bag is empty."