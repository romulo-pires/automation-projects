from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#username")
        self.password_field = page.locator("#password")
        self.flash_message = page.locator("#flash")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_button = page.get_by_role("link", name="Logout")

    def goto(self):
        self.page.goto(self.URL)

    def input_login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def check_successful_login(self):
        expect(self.flash_message).to_contain_text("You logged into a secure area!")
        expect(self.logout_button).to_be_visible()

    def check_invalid_password_error(self):
        expect(self.flash_message).to_contain_text("Your password is invalid!")

    def check_invalid_username_error(self):
        expect(self.flash_message).to_contain_text("Your username is invalid!")

    def check_successful_logout(self):
        self.logout_button.click()
        expect(self.flash_message).to_contain_text("You logged out of the secure area!")
