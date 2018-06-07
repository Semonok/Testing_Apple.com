from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.main_page import MainPage
from Pages.header_block import AllPagesCommonHeader
from Pages.login_page import LoginPage
from Pages.footer_block import AllPagesCommonFooter
from Pages.job_page import JobPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.wait = WebDriverWait(self.driver, 5)
        self.main_page = MainPage(self.driver)
        self.header_block = AllPagesCommonHeader(self.driver)
        self.login_page = LoginPage(self.driver)
        self.footer_block = AllPagesCommonFooter(self.driver)
        self.job_page = JobPage(self.driver)

    def home_page(self):
        self.driver.get("https://www.apple.com/")

    def quit(self):
        self.driver.quit()

    def url_changes_to(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except:
            return False

    @property
    def page_title(self):
        return self.driver.title



