from playwright.sync_api import Page, expect
from .base_page import BasePage


class CartPage(BasePage):
    ITEM = ".cart_item"

    def __init__(self, page: Page):
        super().__init__(page)

    def should_have_item(self, item_name: str):
        expect(self.page.locator(self.ITEM).filter(has_text=item_name)).to_have_count(1)

    def remove_item(self, item_name: str):
        self.page.locator(self.ITEM).filter(has_text=item_name) \
            .locator("button:has-text('Remove')").click()

    def should_not_have_item(self, item_name: str):
        expect(self.page.locator(self.ITEM).filter(has_text=item_name)).to_have_count(0)
