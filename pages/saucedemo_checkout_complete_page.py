from playwright.sync_api import Page, expect

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.complete_header = page.locator(".complete-header")

    def check_loaded(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
        expect(self.complete_header).to_contain_text("Thank you for your order!")