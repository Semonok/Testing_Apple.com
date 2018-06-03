from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.main_page import MainPage
from Pages.common_header import AllPagesCommonHeader

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.wait = WebDriverWait(self.driver, 5)
        self.main_page = MainPage(self.driver)
        self.common_header = AllPagesCommonHeader(self.driver)

    def home_page(self):
        self.driver.get("https://www.apple.com/")

    def quit(self):
        self.driver.quit()

    def new_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @property
    def page_title(self):
        return self.driver.title


