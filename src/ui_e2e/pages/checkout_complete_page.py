from playwright.sync_api import Page, expect
from .base_page import BasePage


class CheckoutCompletePage(BasePage):
    TITLE = ".title"
    COMPLETE_HEADER = ".complete-header"

    def __init__(self, page: Page):
        super().__init__(page)

    def should_be_opened(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Complete!")

    def should_show_success(self):
        expect(self.page.locator(self.COMPLETE_HEADER)).to_have_text("Thank you for your order!")
