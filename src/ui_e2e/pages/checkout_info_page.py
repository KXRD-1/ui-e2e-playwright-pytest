from playwright.sync_api import Page, expect
from .base_page import BasePage


class CheckoutInfoPage(BasePage):
    FIRST_NAME = '[data-test="firstName"]'
    LAST_NAME = '[data-test="lastName"]'
    POSTAL_CODE = '[data-test="postalCode"]'
    CONTINUE_BTN = '[data-test="continue"]'
    TITLE = ".title"

    def __init__(self, page: Page):
        super().__init__(page)

    def should_be_opened(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Your Information")

    def fill_and_continue(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)
        self.page.click(self.CONTINUE_BTN)
