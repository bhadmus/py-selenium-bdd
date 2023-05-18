
class LoginPage:
    """
        This stores element on the homepage
    """
    url = 'https://www.saucedemo.com/'
    user_name_field = '[data-test="username"]'
    password_field = '[data-test="password"]'
    login_button = '[data-test="login-button"]'
    burger_menu = '#react-burger-menu-btn'
    standard = 'standard_user'
    password = 'secret_sauce'
    glitch = 'performance_glitch_user'


class ShopPage:
    """
        This stores element on the product page
    """
    product_header = ".header_secondary_container"
    sauce_labs_backpack = ".inventory_item_name"
    add_cart_button = "[data-test='add-to-cart-sauce-labs-backpack']"
    remove_item = "[data-test='remove-sauce-labs-backpack']"
    cart_icon = ".shopping_cart_link"
    checkout_button = "[data-test='checkout']"


class UserInfo:
    """
        This stores element on the user info page
    """
    fname_field = '[data-test="firstName"]'
    lname_field = '[data-test="lastName"]'
    zipcode_field = '[data-test="postalCode"]'
    continue_button = '[data-test="continue"]'


class CompleteOrder:
    """
        This stores element on the final order product page
    """
    finish_order_button = '[data-test="finish"]'
    total_amount = '.summary_info_label summary_total_label'
    success_message_holder = '.complete-header'
    actual_success_message = 'Thank you for your order!'


class TestData:
    """
        This stores the test data
    """
    fname = 'Eva'
    lname = 'Mendez'
    zip_code = '23401'
    item_name = 'Sauce Labs Backpack'


class LogoutPage:
    """
        This stores element on the logout page
    """
    burger_menu = '#react-burger-menu-btn'
    logout_link = '#logout_sidebar_link'
