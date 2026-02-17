from playwright.sync_api import Page, expect
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME = '[data-test="username"]'
    PASSWORD = '[data-test="password"]'
    LOGIN_BTN = '[data-test="login-button"]'
    ERROR = '[data-test="error"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def should_show_error(self, text_part: str):
        expect(self.page.locator(self.ERROR)).to_contain_text(text_part)
