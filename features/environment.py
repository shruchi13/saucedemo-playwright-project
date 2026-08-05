import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkoutOverview_page import CheckoutOverviewPage

def before_all(context):
    context.playwright = sync_playwright().start()
    # Launch a browser once for the entire test suite; we will create a new context for each scenario
    context.browser = context.playwright.chromium.launch(
        headless=False, slow_mo=500
    )

# Function to start playwright and launch a browser 
def before_scenario(context, scenario):
    # Load storage state if the scenario is tagged with @authenticated 
    # Otherwise, start with a completely fresh browser context for scenarios that don't require authentication
    if os.path.exists("state.json") and "authenticated" in scenario.tags:
        context.browser_context = context.browser.new_context(storage_state ="state.json")
    else:
        context.browser_context = context.browser.new_context()
    # Create a fresh tag/page for this scenario

    context.page = context.browser_context.new_page()    

    # Initialize Page Object on context. Bind page objects to the fresh page instance 

    context.login_page = LoginPage(context.page)
    context.inventory_page = InventoryPage(context.page)
    context.cart_page = CartPage(context.page)
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_overview_page = CheckoutOverviewPage(context.page)

# Function to close browser and stop playwright after finish scenario
def after_scenario(context, scenario):
    # Clean up page and context safety after each scenario

    if hasattr(context, "page") and context.page:
        try:
            context.page.close()
        except:
            pass
    if hasattr(context, "browser_context") and context.browser_context:
        try:
            context.browser_context.close()
        except:
            pass
        context.browser_context.close()

def after_all(context):
    # Clean up browser and playwright after all scenarios have finished
    if hasattr(context, "browser") and context.browser:
        try:
           context.browser.close()  
        except:
                pass

    if hasattr(context, "playwright") and context.playwright:
        try:
            context.playwright.stop()
        except:
            pass
        context.playwright.stop()