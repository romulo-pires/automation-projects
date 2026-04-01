from playwright.sync_api import Page, expect

class ShopPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_button = page.locator(".shopping_cart_link")

    def check_loaded(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def add_fleece_jacket_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()

    def open_cart(self):
        self.cart_button.click()
    

    
