
from behave import *

from resources.page_object import HomePageObject
from data_elements.element_mapper import *

browse = HomePageObject()
use_step_matcher("parse")


@given(u'I am on the sauce demo page')
def step_impl(context):
    browse.launch_page()


@when(u'I insert the standard username')
def step_impl(context):
    browse.fill_details(LoginPage.user_name_field, LoginPage.standard)


@when(u'I insert the "{username}"')
def step_impl(context, username):
    browse.fill_details(LoginPage.user_name_field, username)


@when(u'I insert the password')
def step_impl(context):
    browse.fill_details(LoginPage.password_field, LoginPage.password)


@when(u'I click the "{text}"')
def step_impl(context, text):
    if text == "login button":
        browse.click_element(LoginPage.login_button)
    elif text == "cart icon":
        browse.click_element(ShopPage.cart_icon)


@then(u'I should see the product list page')
def step_impl(context):
    browse.wait_for_text_presence(ShopPage.product_header, 'Product')


@when(u'I add an Item to cart')
def step_impl(context):
    browse.click_element(ShopPage.add_cart_button)


@when(u'I "{action}" item')
def step_impl(context, action):
    if action == "add":
        browse.click_element(ShopPage.add_cart_button)
    elif action == "remove":
        browse.click_element(ShopPage.remove_item)


@when(u'I remove an Item from cart')
def step_impl(context):
    browse.click_element(ShopPage.remove_item)


@then(u'I should see the item in the cart')
def step_impl(context):
    browse.verify_text(ShopPage.sauce_labs_backpack, TestData.item_name)


@then(u'I should see the "{result}"')
def step_impl(context, result):
    if result == "item in cart":
        browse.verify_text(ShopPage.sauce_labs_backpack, TestData.item_name)
    elif result == "empty cart ":
        browse.wait_for_absence(ShopPage.sauce_labs_backpack)


@then(u'I should not see the item in the cart')
def step_impl(context):
    browse.wait_for_absence(ShopPage.sauce_labs_backpack)


@then(u'I logout')
def step_impl(context):
    browse.click_element(LogoutPage.burger_menu)
    browse.click_element(LogoutPage.logout_link)


@when(u'I insert the glitch username')
def step_impl(context):
    browse.fill_details(LoginPage.user_name_field, LoginPage.glitch)


@then(u'I should see the following on the product page')
def step_impl(context):
    for row in context.table:
        from selenium.webdriver.support import expected_conditions
        from selenium.webdriver.common.by import By
        browse.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, '#root'), row["Items"]))



