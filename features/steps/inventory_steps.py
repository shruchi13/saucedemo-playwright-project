from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

@given('I am logged in as a "{username}"')
def step_impl(context, username):
    # Initialize page object as the start 
    context.login_page = LoginPage(context.page)
    context.inventory_page = InventoryPage(context.page)

    # Navigate directly to inventory; state.json handles authentication state automatically
    # context.page.goto("https://www.saucedemo.com/inventory.html")
    
    # Fallback: If redirected back to login page (e.g. state expired/missing), log in via UI
    #if "inventory.html" not in context.page.url:
        #context.login_page = LoginPage(context.page)
        #context.inventory_page = InventoryPage(context.page)
        # Navigate to Login page
       # context.login_page.navigate()
    # Perform UI login directly to guarantee valid session state
    context.login_page.login(username, "secret_sauce")
    
    # Ensure inventory page is completely loaded before downstream steps run 
    context.inventory_page.is_loaded()


@then('I should see the page title "{expected_title}"')
def step_impl(context, expected_title):
    expect(context.inventory_page.title).to_have_text(expected_title)

@then('there should be {count:d} products displayed')
def step_impl(context, count):
    expect(context.inventory_page.inventory_items).to_have_count(count)

@when('I add "{item_name}" to the cart')
def step_impl(context, item_name):
    context.inventory_page.add_item_to_cart(item_name)

@when('I remove item "{item_name}" from the inventory page')
def step_impl(context, item_name):
    context.inventory_page.remove_item_from_cart(item_name)

@then('the shopping cart badge count should be "{expected_count}"')
def step_impl(context, expected_count):
    if expected_count == "0":
        expect(context.inventory_page.shopping_cart_badge).to_be_hidden()
    else:
        expect(context.inventory_page.shopping_cart_badge).to_have_text(expected_count)

@when('I sort products by "{sort_option}"')
def step_impl(context, sort_option):
    context.inventory_page.sort_products_by(sort_option)

@then('the products should be sorted by price in ascending order')
def step_impl(context):
    prices = context.inventory_page.get_all_product_prices()
    assert prices == sorted(prices), f"Prices are not sorted: {prices}"

@then('the products should be sorted by price in decending order')
def step_impl(context):
    prices = context.inventory_page.get_all_product_prices()
    assert prices == sorted(prices, reverse=True), f"Prices are not in descending order: {prices}"

@then('the products should be sorted alphabetically from A to Z')
def step_impl(context):
    names = context.inventory_page.get_all_product_names()
    assert names == sorted(names), f"Products are not sorted A to Z: {names}"

@then('the products should be sorted alphabetically from Z to A')
def step_impl(context):
    names = context.inventory_page.get_all_product_names()
    assert names == sorted(names, reverse=True), f"Products are not sorted Z to A: {names}"
