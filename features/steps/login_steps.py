from behave import given, when,then
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from playwright.sync_api import expect
# Naviagte to login page
@given("I navigate to SauceDemo login page")
def step_impl(context):
    context.login_page =LoginPage(context.page)
    context.login_page.navigate()

# Use placeholders "{username}" and "{password}" so Behave passes them into step_impl
@when('I log in with username "{username}" and password "{password}"')
def step_impl(context,username,password):
    context.login_page.enter_credentials(username,password)
    context.login_page.click_login_button()

@then("I should be redirected to the inventory page")
def step_impl(context):
    #Perform assertion directly on context page
    context.inventory_page = InventoryPage(context.page)
    context.inventory_page.is_loaded()
    expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")

@then('I should see an error message "{expected_msg}"')
def step_impl(context, expected_msg):
    assert context.login_page.error_message.is_visible()
    actual_message = context.login_page.error_message.text_content()
    assert expected_msg in actual_message, f"Expected '{expected_msg}' in error message, but got '{actual_message}'"