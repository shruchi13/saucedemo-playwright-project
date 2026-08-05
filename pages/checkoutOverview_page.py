# Checkout Overview Page Object Model (POM) class
from playwright.sync_api import Page, expect

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_overview_title = page.locator(".title")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.cart_item_names = page.locator(".inventory_item_name")
        self.cart_item_prices = page.locator(".inventory_item_price")
        self.cart_item_quantities = page.locator(".cart_quantity")
        self.item_total_label = page.locator(".summary_subtotal_label")
        self.tax_label = page.locator(".summary_tax_label")
        self.total_label = page.locator(".summary_total_label")

    def click_finish(self):
        self.finish_button.click()

    def click_cancel(self):
        self.cancel_button.click()

    def get_cart_item_names(self) -> list[str]:
        return self.cart_item_names.all_text_contents()

    def get_cart_item_prices(self) -> list[str]:
        return self.cart_item_prices.all_text_contents()
    
    def get_cart_item_quantities(self) -> list[str]:
        return self.cart_item_quantities.all_text_contents()

    def get_item_total(self) -> str:
        return self.item_total_label.text_content()

    def get_tax(self) -> str:
        return self.tax_label.text_content()

    def get_total(self) -> str:
        return self.total_label.text_content()
    
    def get_payment_info(self) -> str:
        return self.page.locator(".summary_value_label").nth(0).text_content()
    
    def get_shipping_info(self) -> str:
        return self.page.locator(".summary_value_label").nth(1).text_content()