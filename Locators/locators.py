from selenium.webdriver.common.by import By

class HeaderLocators:

    country_selection_menu = (By.XPATH, "//div[@id='ac-ls-dropdown-select']")
    choose_country         = (By.XPATH, "//li[@id='ac-ls-dropdown-option-country-region']")
    accept_region          = (By.XPATH, "//a[@id='ac-ls-continue']")
    home_page              = (By.XPATH, "//a[@id='ac-gn-firstfocus']")
    mac_page               = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-mac']")
    ipad_page              = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-ipad']")
    iphone_page            = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-iphone']")
    watch_page             = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-watch']")
    appletv_page           = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-tv']")
    music_page             = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-music']")
    support_page           = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-support']")
    search_menu            = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-search']")
    settings_menu          = (By.XPATH, "//li[@id='ac-gn-bag']/a")
    bag_page               = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-bag']")
    favotites_page         = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-favorites']")
    orders_page            = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-orders']")
    account_page           = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-account']")
    sign_in_page           = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signIn']")
    sign_out               = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signOut']")
    quick_link             = (By.XPATH, "//li[@class='ac-gn-searchresults-item ac-gn-searchresults-animated']/a")
    search_field           = (By.XPATH, "//input[@id='ac-gn-searchform-input']")


class MainPageLocators:    # 9 items total

    first_item   = (By.XPATH, "//li[@id='section-1-hero-position-1']//a")
    second_item  = (By.XPATH, "//li[@id='section-1-hero-position-2']//a")
    third_item   = (By.XPATH, "//li[@id='section-1-hero-position-3']//a")
    fourth_item  = (By.XPATH, "//li[@id='section-2-promo-position-1']//a")
    fifth_item   = (By.XPATH, "//li[@id='section-2-promo-position-2']//a")
    sixth_item   = (By.XPATH, "//li[@id='section-2-promo-position-3']//a")
    seventh_item = (By.XPATH, "//li[@id='section-2-promo-position-4']//a")
    eighth_item  = (By.XPATH, "//li[@id='section-2-promo-position-5']//a")
    ninth_item   = (By.XPATH, "//li[@id='section-2-promo-position-6']//a")


class FooterLocators:

    footer_up         = (By.XPATH, "//a[@class='ac-gf-directory-column-section-link']") # 28 links
    footer_legal      = (By.XPATH, "//a[@class='ac-gf-footer-legal-links']") # 6 links
    footer_country    = (By.XPATH, "//a[@class='ac-gf-footer-locale-link']") # 1 link
    job_at_apple_link = (By.XPATH, "//a[@href='/jobs/us/']")

class LoginPageLocators:

    login          = (By.XPATH, "//input[@type='email']")
    login_error    = (By.XPATH, "//div[@id='loginHome.customerLogin.appleId-error']")
    password       = (By.XPATH, "//input[@type='password']")
    password_error = (By.XPATH, "//div[@id='loginHome.customerLogin.password-error']")
    confirm_button = (By.XPATH, "//button[@id='signin-button-submit']")
    main_error     = (By.XPATH, "//div[@class='form-alert is-error']")


class CountryListPageLocators:
    # Choose country region locators (128 total)
    select_country = (By.XPATH, "//a[@class='block']") # Maybe later I will write all unique locators on this page

class JobPageLocators:
    open_search_job_page = (By.XPATH, "//ul[@class='no-margin no-padding']/li[5]/a")

class FavoritesPageLocators:
    empty_list = (By.XPATH, "//div[@id='empty-list-message']")
    item_name  = (By.XPATH, "//h2[@class='rs-favorites-item-heading']")

class BagPageLocators:
    bag_main_text = (By.XPATH, "//h1[@class='rs-bag-header']")

class IphonePageLocators:
    iphone_x    = (By.XPATH, "//li[@class='chapternav-item chapternav-item-overview']/a")
    iphone_8    = (By.XPATH, "//li[@class='chapternav-item chapternav-item-iphone-8']/a")
    iphone_7    = (By.XPATH, "//li[@class='chapternav-item chapternav-item-iphone-7']/a")
    iphone_6s   = (By.XPATH, "//li[@class='chapternav-item chapternav-item-iphone-6s']/a")
    iphone_se   = (By.XPATH, "//li[@class='chapternav-item chapternav-item-iphone-se']/a")
    ios_11      = (By.XPATH, "//li[@class='chapternav-item chapternav-item-ios']/a")
    accessories = (By.XPATH, "//li[@class='chapternav-item chapternav-item-accessories']/a")
    compare     = (By.XPATH, "//li[@class='chapternav-item chapternav-item-compare']/a")

class MacPageLocators:
    macbook      = (By.XPATH, "//li[@class='chapternav-item chapternav-item-macbook macbook']/a")
    macbook_air  = (By.XPATH, "//li[@class='chapternav-item chapternav-item-macbook-air macbook-air']/a")
    macbook_pro  = (By.XPATH, "//li[@class='chapternav-item chapternav-item-macbook-pro macbook-pro']/a")
    imac_pro_buy = (By.XPATH, "//section[@class='fp-product product-imac-pro section theme-dark']//a[2]")

class ImacProBuyPageLocators:
    favorites_button = (By.XPATH, "//button[@class='fv-link as-heart favorites  ']")





