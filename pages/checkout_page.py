from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_info_title = page.locator(".title")
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.error_message = page.locator("[data-test='error']")


    def enter_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)       

    def click_continue(self):
        self.continue_button.click()    

    def click_cancel(self):
        self.cancel_button.click()

    def get_error_message(self) -> str:
            return self.error_message.text_content() 
    

    
    
