#pages/cart_page.py
from playwright.sync_api import Page
class CartPage:
    def __init__(self,page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.cart_item_name = page.locator(".inventory_item_name")
        self.cart_item_prices = page.locator(".inventory_item_price")
        self.checkout_button = page.get_by_role("button", name = "checkout")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.cart_quantity = page.locator(".cart_quantity")
        

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def get_cart_item_names(self) -> list[str]:
        return self.cart_item_name.all_text_contents()
    
    def get_cart_item_count(self) -> int:
        return self.cart_items.count()
    
    def remove_item(self,item_name: str):
        item_container = self.cart_items.filter(has_text=item_name)
        item_container.get_by_role("button", name ="Remove").click()

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

