# Should be 5 quick links in search menu
def test_checking_presence_of_quick_links(driver):
    driver.header_block.open_search()
    assert driver.header_block.five_quick_links_are_present == True