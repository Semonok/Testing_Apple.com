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
    settings_menu          = (By.XPATH, "//a[@class='ac-gn-link ac-gn-link-bag']")
    bag_page               = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-bag']")
    favotites_page         = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-favorites']")
    orders_page            = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-orders']")
    account_page           = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-account']")
    sign_in_page           = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signIn']")
    sign_out               = (By.XPATH, "//a[@class='ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signOut']")


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

    footer_up      = (By.XPATH, "//a[@class='ac-gf-directory-column-section-link']") # 28 links
    footer_legal   = (By.XPATH, "//a[@class='ac-gf-footer-legal-links']") # 6 links
    footer_country = (By.XPATH, "//a[@class='ac-gf-footer-locale-link']") # 1 link

class LoginPageLocators:

    login          = (By.XPATH, "//input[@type='email']")
    login_error    = (By.XPATH, "//div[@id='loginHome.customerLogin.appleId-error']")
    password       = (By.XPATH, "//input[@type='password']")
    password_error = (By.XPATH, "//div[@id='loginHome.customerLogin.password-error']")
    confirm_button = (By.XPATH, "//button[@id='signin-button-submit']")
    main_error     = (By.XPATH, "//div[@class='form-alert is-error']")


class CountryRegionPageLocators:
    # Choose country region locators (128 total)
    select_country = (By.XPATH, "//a[@class='block']") # Maybe later I will write all unique locators on this page




