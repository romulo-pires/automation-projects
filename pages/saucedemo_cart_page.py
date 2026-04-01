from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")

    def check_loaded(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")

    def click_checkout(self):
        self.checkout_button.click()