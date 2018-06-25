
def test_add_gift_card_empty_message(driver):
    driver.header_block.open_mac_page()
    driver.mac_page.open_buy_page_imac_pro()
    driver.imac_pro_buy_page.open_customize_page()
    driver.customize_imac_pro_buy_page.add_to_bag()
    driver.imac_pro_accessories_page.review_bag()
    assert "iMac Pro" in driver.bag_page.items
    driver.bag_page.open_gift_card()
    driver.gift_card_block.write_message("")
    driver.gift_card_block.save_changes()
    assert driver.gift_card_block.alert == "Please enter a gift message to continue with your order."

def test_add_gift_card_message(driver):
    message = 'With love'
    driver.gift_card_block.write_message(message)
    driver.gift_card_block.save_changes()
    assert driver.bag_page.gift_message_text == message

def test_alert_gift_message_if_item_quantity_more_ten(driver):
    driver.bag_page.choose_item_quantity(10)
    assert driver.bag_page.alert_message_is_not_presence == True
    driver.bag_page.choose_item_quantity(11)
    assert driver.bag_page.alert_message == "We’re unable to add gift messages to orders of this size. Please call 1‑800‑MY‑APPLE for help with this request."
    driver.bag_page.choose_item_quantity(1)
    assert driver.bag_page.alert_message_is_not_presence == True

def test_edit_gift_message(driver):
    message = 'Again'
    driver.bag_page.edit_gift_card()
    driver.gift_card_block.write_message(message)
    driver.gift_card_block.save_changes()
    assert driver.bag_page.gift_message_text == message

def test_remove_gift_message(driver):
    driver.bag_page.edit_gift_card()
    driver.gift_card_block.remove_message()
    driver.gift_card_block.save_changes()
    assert driver.bag_page.gift_message_text == None



