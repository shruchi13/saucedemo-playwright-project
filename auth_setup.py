from playwright.sync_api import sync_playwright

def generate_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        # Perform login 
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Save session storage/cookie state
        context.storage_state(path="state.json")
        print("Saved login state to state.json")
        browser.close()

if __name__=="__main__":
    generate_auth_state()   
