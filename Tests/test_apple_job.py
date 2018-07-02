
def test_check_search_job_page(driver):
    driver.footer_block.open_job_page()
    driver.job_page.open_search_job_page()
    assert driver.current_page("Job page") == True