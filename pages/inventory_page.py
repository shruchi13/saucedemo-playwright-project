from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_link = page.locator(".shopping_cart_link")

    def is_loaded(self):
        # Wait until page URL and title are ready
        self.page.wait_for_url("**/inventory.html", timeout =10000)
        self.title.wait_for(state="visible", timeout =10000)
        self.inventory_items.first.wait_for(state="visible", timeout =10000)

    def get_title_text(self) -> str:
        return self.title.inner_text()
    
    def get_item_count(self) -> int:
        return self.inventory_items.count()
    
    def add_item_to_cart(self, item_name: str):
        # Ensure page element are ready 
        self.is_loaded()
        # Convert item name to SauceDemo data-test attribute format
        item_slug = item_name.lower().replace(" ", "-")
        add_btn = self.page.locator(f"[data-test='add-to-cart-{item_slug}']")
        # Resilient fallback if data-test selector doesn't match
        if not add_btn.is_visible(timeout=2000):
            item_container = self.inventory_items.filter(has_text=item_name)
            add_btn = item_container.locator("button", has_text="Add to cart")
        add_btn.click()

    def remove_item_from_cart(self, item_name: str):
        self.is_loaded()
        item_slug = item_name.lower().replace(" ", "-")
        remove_btn = self.page.locator(f"[data-test='remove-{item_slug}']")
        if not remove_btn.is_visible(timeout=2000):
            item_container =self.inventory_items.filter(has_text=item_name)
            remove_btn = item_container.locator("button", has_text="Remove")

        remove_btn.click()


    def sort_products_by(self, option_value: str):
        # Normalizing spaces and case so 'Name(A to Z)' or 'Name (A to Z)' both work
        cleaned_value = option_value.replace(" ", "").lower()
        sort_map = {
            "name(atoz)": "az",
            "name(ztoa)": "za",
            "price(lowtohigh)": "lohi",
            "price(hightolow)": "hilo"
        }
        val = sort_map.get(cleaned_value, option_value)
        self.sort_dropdown.select_option(val)

    def get_all_product_prices(self) -> list[float]:
        # .all_text_contents() extracts list of strings before iterating
        price_strings = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(price.replace("$", "")) for price in price_strings]
    
    def get_all_product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()
    
    def get_cart_count(self) -> str:
        if self.shopping_cart_badge.is_visible():
            return self.shopping_cart_badge.text_content().strip()
        return "0"
