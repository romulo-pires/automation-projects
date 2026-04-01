from pages.login_page import LoginPage


def test_login_success(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.input_login("tomsmith", "SuperSecretPassword!")
    login_page.check_successful_login()


def test_login_with_invalid_password(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.input_login("tomsmith", "senha_errada")
    login_page.check_invalid_password_error()


def test_login_with_invalid_username(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.input_login("usuario_errado", "SuperSecretPassword!")
    login_page.check_invalid_username_error()

def test_logout(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.input_login("tomsmith", "SuperSecretPassword!")
    login_page.check_successful_login()
    login_page.check_successful_logout()