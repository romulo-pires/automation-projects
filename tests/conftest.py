import pytest
from pages.saucedemo_login_page import LoginPage
from pages.saucedemo_shop_page import ShopPage

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    shop_page = ShopPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    shop_page.check_loaded()

    return page