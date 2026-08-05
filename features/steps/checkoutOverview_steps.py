from behave import given,when, then
from playwright.sync_api import expect, Playwright
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkoutOverview_page import CheckoutOverviewPage

@when('I see the checkout overview page')
@then('I see the checkout overview page')
@then('I should see the checkout overview page')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    expect(context.checkout_overview_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

@then('I should see "{item_name}" in the checkout overview')
def step_impl(context, item_name):
    
    cart_item_names = context.checkout_overview_page.get_cart_item_names()
    assert item_name in cart_item_names, f"Expected '{item_name}' in cart, got: {cart_item_names}"

@then('I should see item price in the checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    prices = context.checkout_overview_page.get_cart_item_prices()
    assert len(prices) > 0, "Expected item prices to be displayed in the checkout overview."

@then('I should see item quantity in the checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    quantities = context.checkout_overview_page.get_cart_item_quantities()
    assert len(quantities) > 0, "Expected item quantities to be displayed in the checkout overview."
    
@then('I should see the total price in the checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    item_total = context.checkout_overview_page.get_item_total()
    assert "Item total:"in item_total ,f"Unexpected item total format: {item_total}"
    
@then('I should see the tax amount in the checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    tax = context.checkout_overview_page.get_tax()
    assert "Tax:" in tax, f"Unexpected tax format: {tax}"

@then('I should see the final total price in the checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    total = context.checkout_overview_page.get_total()
    assert "Total:" in total, f"Unexpected total format: {total}"

@then('I should see Payment Information in the checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    payment_info = context.checkout_overview_page.get_payment_info()
    assert payment_info is not None and len(payment_info) > 0, "Expected Payment Information to be displayed in the checkout overview."
    
@then('I should see Shipping Information in the checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    shipping_info = context.checkout_overview_page.get_shipping_info()
    assert shipping_info is not None and len(shipping_info) > 0, "Expected Shipping Information to be displayed in the checkout overview."
    
@when('I click Finish button')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    context.checkout_overview_page.click_finish()   

@then('I should be redirected to the checkout complete page')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")   

@then('I should see a confirmation message "{expected_message}"')
def step_impl(context, expected_message):
    actual_message = context.page.locator(".complete-header").text_content()
    assert actual_message == expected_message, f"Expected confirmation message to be '{expected_message}', but got '{actual_message}'"

@when('I click Cancel button on the checkout overview page')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    context.checkout_overview_page.click_cancel()

@then('I should be redirected back to the inventory page')
@then('I should be redirected back to the inventory page from the checkout overview page')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")   
