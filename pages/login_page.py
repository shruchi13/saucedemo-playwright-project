# Implement Page Object model (POM)
# Create isolate element locators and actions 
from playwright.sync_api import sync_playwright, Page


class LoginPage:
    # Initiate all locators
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_btn = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
    # Function to navigate the requested website 
    def navigate(self):
        self.page.goto("https://www.saucedemo.com")
    
    # Function to enter username and password
    def enter_credentials(self,username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)

    # Function to click login button
    def click_login_button(self):
        self.login_btn.click()

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    # Check if login succeeded by checking if error is not displayed 
        if not self.error_message.is_visible():
         self.page.wait_for_url("**/inventory.html")
    

    

        
       