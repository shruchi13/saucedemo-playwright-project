from behave import given, when, then
from playwright.sync_api import expect, Playwright
from pages.inventory_page import InventoryPage


@when('I go to shopping cart')
def step_impl(context):
    context.inventory_page.shopping_cart_link.click()

@then('cart Page should load')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(context.cart_page.title).to_have_text("Your Cart")

@then('I should see "{item_name}" in the cart')
def step_impl(context, item_name):
    items = context.cart_page.get_cart_item_names()
    assert item_name in items, f"Expected '{item_name}' to be in the cart, but got {items}"

@then('I should see item price in the cart')
def step_impl(context):
    expect(context.cart_page.cart_item_prices.first).to_be_visible()

@then ('I should see item quantity in the cart')
def step_impl(context):
    expect(context.cart_page.cart_quantity.first).to_be_visible()

@when('I click checkout button')
def step_impl(context):
    context.cart_page.proceed_to_checkout()

@then('I navigate to checkout page')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

@when('I remove "{item_name}" from the cart page')
def step_impl(context, item_name):
    context.cart_page.remove_item(item_name)

@then(('"{item_name}" should not be in the cart'))
def step_impl(context, item_name):
    items = context.cart_page.get_cart_item_names()
    assert item_name not in items, f"Expected {item_name} to be removed from the cart, but got {items}"   

@when('I click continue shopping button')
def step_impl(context):
    context.cart_page.continue_shopping()

@then('I navigate back to inventory page')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")


