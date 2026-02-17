from playwright.sync_api import Page, expect
from .base_page import BasePage


class InventoryPage(BasePage):
    TITLE = ".title"
    SORT = "select.product_sort_container, [data-test='product_sort_container']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def __init__(self, page: Page):
        super().__init__(page)

    def should_be_opened(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Products")

    def add_item(self, item_name: str):
        self.page.locator(".inventory_item").filter(has_text=item_name) \
            .locator("button:has-text('Add to cart')").click()

    def remove_item(self, item_name: str):
        self.page.locator(".inventory_item").filter(has_text=item_name) \
            .locator("button:has-text('Remove')").click()

    def cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        if badge.count() == 0:
            return 0
        return int(badge.inner_text())

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def sort_by(self, value: str):
        sort = self.page.locator(self.SORT).first
        sort.wait_for(state="visible")
        sort.select_option(value)

    def first_item_name(self) -> str:
        return self.page.locator(".inventory_item_name").first.inner_text()
