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
    item_in_bag            = (By.XPATH, "//span[@class='ac-gn-bagview-bagitem-column2']")


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

    login          = (By.XPATH, "//input[@id='loginHome.customerLogin.appleId']")
    login_error    = (By.XPATH, "//div[@id='loginHome.customerLogin.appleId-error']")
    password       = (By.XPATH, "//input[@id='loginHome.customerLogin.password']")
    password_error = (By.XPATH, "//div[@id='loginHome.customerLogin.password-error']")
    confirm_button = (By.XPATH, "//button[@id='signin-button-submit']")
    main_error     = (By.XPATH, "//div[@class='form-alert is-error']")


class CountryListPageLocators:
    # Choose country region locators (128 total)
    select_country = (By.XPATH, "//a[@class='block']") # Maybe later I will write all unique locators on this page

class JobPageLocators:
    open_search_job_page = (By.XPATH, "//ul[@class='no-margin no-padding']/li[5]/a")

class FavoritesPageLocators:
    empty_list                        = (By.XPATH, "//div[@id='empty-list-message']")
    item_name                         = (By.XPATH, "//h2[@class='rs-favorites-item-heading']")
    edit_remove                       = (By.XPATH, "//button[@id='favorites-edit-items']")
    select_item                       = (By.XPATH, "//span[@class='form-choice-indicator rs-favorites-checkboxicon']")
    select_item_relative_by_edit_name = (By.XPATH, "../../../../../../../../../li//"
        "span[@class='form-choice-indicator rs-favorites-checkboxicon']")
    cancel                            = (By.XPATH, "//button[@class='favorites-cancel-items']")


class BagPageLocators:
    bag_main_text          = (By.XPATH, "//h1[@class='rs-bag-header']")
    items_name             = (By.XPATH, "//h2[@class='rs-iteminfo-title']")
    item_price             = (By.XPATH, "//p[@class='rs-iteminfo-price']")
    subtotal_price         = (By.XPATH, '//div[@data-autom="bagrs-summary-subtotalvalue"]')
    summary_tax_value      = (By.XPATH, '//div[@data-autom="bagrs-summary-taxvalue"]')
    total_price            = (By.XPATH, "//div[@class='rs-summary-content  rs-summary-total']/div[@class='rs-summary-value']")
    remove                 = (By.XPATH, '//button[@class="as-buttonlink rs-iteminfo-remove"]')
    continue_shopping      = (By.XPATH, '//a[@class="button form-button button-secondary"]')
    quantity_less_ten      = (By.XPATH, '//select[@class="rs-quantity-dropdown form-dropdown"]')
    quantity_more_ten      = (By.XPATH, '//input[@class="form-textbox form-textbox-entered"]')
    enter_zip_code         = (By.XPATH, '//button[@id="rs-summary-enterzipcode"]')
    zip_code_field         = (By.XPATH, '//input[@id="shoppingCart.summary.taxCalculator.address.postalCode"]')
    zip_code_apply         = (By.XPATH, '//button[@data-autom="bag-zipcode-apply"]')
    zip_code_cancel        = (By.XPATH, '//button[@id="rr-toggle-shoppingCart.summary.taxCalculator.address._editing"]')
    zip_code_error         = (By.XPATH, '//div[@id="shoppingCart.summary.taxCalculator.address.postalCode-error"]')
    applecare_plus_add     = (By.XPATH, '//button[@data-autom="bag-inlineattach-add"]')
    applecare_plus_price   = (By.XPATH, '//p[@class="rs-iteminfo-child-price"]')
    applecare_plus_remove  = (By.XPATH, '//p[@class="rs-iteminfo-child-price"]/../../div/button')
    gift_message_add       = (By.XPATH, '//button[@data-autom="bag-gifting-add"]')
    gift_message_edit      = (By.XPATH, '//button[@data-autom="bag-giftmessage-edit"]')
    gift_message_text      = (By.XPATH, '//p[@class="rs-iteminfo-child-tagline rs-iteminfo-gifting-msg"]')
    alert_message = (By.XPATH, "//div[@class='form-alert is-error']")

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
    imac_pro_buy = (By.XPATH, "//a[@href='/us/shop/goto/buy_mac/imac_pro']")

class ImacProBuyPageLocators:
    add_favorites_button    = (By.XPATH, "//button[@class='fv-link as-heart favorites  ']")
    remove_favorites_button = (By.XPATH, "//button[@class='fv-link as-heart favorites as-heart-isadded ']")
    configure               = (By.XPATH, "//button[@class='button as-button-large as-button-block']")

class CustomizeImacProPageLocators:
    add_to_bag = (By.XPATH, "//button[@name='add-to-cart']")

class ImacProAccessoriesPageLocators:
    review_bag = (By.XPATH, "//button[@class='merchandising button']")

class GiftCardBlockLocators:
    gift_header        = (By.XPATH, '//h2[@class="rs-giftoverlay-header"]')
    gift_none          = (By.XPATH, "//input[@data-autom='bag-giftoptions-none']"
                                    "/..//div[@class='form-choiceselectorlabel-twocol']")
    gift_message       = (By.XPATH, "//input[@data-autom='bag-giftoptions-message']"
                                    "/..//div[@class='form-choiceselectorlabel-twocol']")
    gift_message_text  = (By.XPATH, "//textarea[@data-autom='bag-giftoptions-messagetext']")
    gift_save_button   = (By.XPATH, "//button[@data-autom='bag-giftoptions-save-button']")
    gift_cancel_button = (By.XPATH, "//button[@data-autom='bag-giftoptions-cancel-button']")
    gift_error_message = (By.XPATH, "//div[@class='form-message-wrapper']")
    gift_overlay_text  = (By.XPATH, "//span[@class='rs-giftoverlay-inputmsg']")




