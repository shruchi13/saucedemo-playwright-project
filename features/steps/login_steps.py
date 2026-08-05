from behave import given, when,then
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
    expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")

@then('I should see an error message "{expected_msg}"')
def step_impl(context, expected_msg):
    expect(context.page.locator("[data-test='error']")).to_contain_text(expected_msg)