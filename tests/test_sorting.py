import pytest
from ui_e2e.pages.login_page import LoginPage
from ui_e2e.pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_sorting_za_sorts_names_desc(page):
    login = LoginPage(page)
    login.open("/")
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.should_be_opened()

    inv.sort_by("za")

    names = page.locator(".inventory_item_name").all_inner_texts()
    assert names == sorted(names, reverse=True)
