from playwright.sync_api import Page, expect

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator("#finish")

    def check_loaded(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    def finish(self):
        self.finish_button.click()