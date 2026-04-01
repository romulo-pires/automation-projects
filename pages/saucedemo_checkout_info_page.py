from playwright.sync_api import Page, expect

class CheckoutInfoPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("#first-name")
        self.last_name_field = page.locator("#last-name")
        self.zip_code_field = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

    def check_loaded(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    def fill_information(self, first_name: str, last_name: str, zip_code: str):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.zip_code_field.fill(zip_code)

    def continue_checkout(self):
        self.continue_button.click()