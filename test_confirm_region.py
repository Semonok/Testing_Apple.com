from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_confirm_region(driver):
    driver.get("https://www.apple.com/")
    driver.find_element_by_css_selector("a#ac-ls-continue").click()
    WebDriverWait(driver,5).until(EC.url_to_be("https://www.apple.com/ru/"))
    assert driver.title == "Apple (Россия) – Официальный сайт"