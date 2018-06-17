from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.json_data import JsonActions
from Pages.main_page import MainPage
from Pages.header_block import AllPagesCommonHeader
from Pages.login_page import LoginPage
from Pages.footer_block import AllPagesCommonFooter
from Pages.job_page import JobPage
from Pages.country_list_page import CountryListPage
from Pages.favorites_page import FavoritesPage
from Pages.bag_page import BagPage
from Pages.iphone_page import IphonePage
from Pages.mac_page import MacPage
from Pages.imac_pro_buy_page import ImacProBuyPage
from Pages.customize_imac_pro_page import CustomizeImacProPage
from Pages.imac_pro_accessories_page import ImacProAccessoriesPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 5)
        self.myjson = JsonActions()
        self.main_page = MainPage(self.driver)
        self.header_block = AllPagesCommonHeader(self.driver)
        self.login_page = LoginPage(self.driver)
        self.footer_block = AllPagesCommonFooter(self.driver)
        self.job_page = JobPage(self.driver)
        self.country_list_page = CountryListPage(self.driver)
        self.favorites_page = FavoritesPage(self.driver)
        self.bag_page = BagPage(self.driver)
        self.iphone_page = IphonePage(self.driver)
        self.mac_page = MacPage(self.driver)
        self.imac_pro_buy_page = ImacProBuyPage(self.driver)
        self.customize_imac_pro_buy_page = CustomizeImacProPage(self.driver)
        self.imac_pro_accessories_page = ImacProAccessoriesPage(self.driver)

    def home_page(self):
        self.driver.get("https://www.apple.com/")

    def quit(self):
        self.driver.quit()

    @property
    def url(self):
        return self.driver.current_url

    @property
    def page_title(self):
        return self.driver.title

    def current_page(self, page):
        try:
            self.wait.until(EC.title_is(self.myjson.read_json_file("pages_title_standart.json")[page]))
            return True
        except:
            print("This is other page, check 'pages_title_standart.json'")
            return False

    @property
    def login_data(self):
        try:
            return self.myjson.read_json_file("login_data.json")
        except:
            print("File not found, check 'data' directory and found jsonfile with 'sign in' data")


