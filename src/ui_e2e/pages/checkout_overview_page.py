from playwright.sync_api import Page, expect
from .base_page import BasePage


class CheckoutOverviewPage(BasePage):
    FINISH_BTN = '[data-test="finish"]'
    TITLE = ".title"

    def __init__(self, page: Page):
        super().__init__(page)

    def should_be_opened(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Overview")

    def finish(self):
        self.page.click(self.FINISH_BTN)
