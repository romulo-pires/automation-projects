from pages.saucedemo_login_page import LoginPage
from pages.saucedemo_shop_page import ShopPage
from pages.saucedemo_cart_page import CartPage
from pages.saucedemo_checkout_info_page import CheckoutInfoPage
from pages.saucedemo_checkout_overview_page import CheckoutOverviewPage
from pages.saucedemo_checkout_complete_page import CheckoutCompletePage

def test_login(page):
    login_page = LoginPage(page)
    shop_page = ShopPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    shop_page.check_loaded()

def test_checkout_flow(logged_in_page):
    shop_page = ShopPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_info_page = CheckoutInfoPage(logged_in_page)
    checkout_overview_page = CheckoutOverviewPage(logged_in_page)
    checkout_complete_page = CheckoutCompletePage(logged_in_page)

    shop_page.add_fleece_jacket_to_cart()
    shop_page.open_cart()

    cart_page.check_loaded()
    cart_page.click_checkout()

    checkout_info_page.check_loaded()
    checkout_info_page.fill_information("Nome", "Sobrenome", "12345")
    checkout_info_page.continue_checkout()

    checkout_overview_page.check_loaded()
    checkout_overview_page.finish()

    checkout_complete_page.check_loaded()

