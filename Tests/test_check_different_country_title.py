
def test_country_links(driver):
    driver.footer_block.open_country_list()
    driver.country_list_page.checking_country_links()