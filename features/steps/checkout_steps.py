from behave import given, use_step_matcher, when, then
from playwright.sync_api import expect, Playwright
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# Switch to Regex matcher to allow matching empty strings ("")
use_step_matcher("re")


@when(r'I fill in checkout information with first name "(?P<first_name>.*?)", last name "(?P<last_name>.*?)", and postal code "(?P<postal_code>.*?)"')
def step_impl_fill_checkout(context, first_name, last_name, postal_code):
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_page.enter_checkout_information(first_name, last_name, postal_code)


# Switch back to standard parse matcher for remaining steps
use_step_matcher("parse")
   
@when('I click continue button')
@then('I click continue button')
def step_impl(context):
    context.checkout_page.click_continue()

#Registered as both @when and @then to match any Gherkin keyword used
@when('I click Cancel button')
@then("I click Cancel button")
def step_impl(context):
    context.checkout_page.click_cancel()

#@then('I should see the checkout overview page')
@then('I see checkout Overview title')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(context.checkout_page.checkout_info_title).to_have_text("Checkout: Overview")

@then('I should be redirected back to the shopping cart page')
def step_impl_redirect_cart(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/cart.html")

@then('I should see the error message "{expected_error_message}"')
def step_impl(context, expected_error_message):
    actual_error_message = context.checkout_page.get_error_message()
    assert expected_error_message in actual_error_message, f"Expected '{expected_error_message}',got: '{actual_error_message}'"