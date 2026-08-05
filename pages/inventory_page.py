from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_link = page.locator(".shopping_cart_link")

    def get_title_text(self) -> str:
        return self.title.inner_text()
    
    def get_item_count(self) -> int:
        return self.inventory_items.count()
    
    def add_item_to_cart(self, item_name: str):
        item_container = self.page.locator(".inventory_item").filter(has_text=item_name)
        item_container.get_by_role("button", name="Add to cart").click()

    def remove_item_from_cart(self, item_name: str):
        item_container = self.page.locator(".inventory_item").filter(has_text=item_name)
        item_container.get_by_role("button", name="Remove").click()


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
