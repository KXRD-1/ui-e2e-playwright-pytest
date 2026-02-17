import pytest
from ui_e2e.pages.login_page import LoginPage
from ui_e2e.pages.inventory_page import InventoryPage
from ui_e2e.pages.cart_page import CartPage

ITEM = "Sauce Labs Backpack"


@pytest.mark.smoke
def test_add_to_cart(page):
    login = LoginPage(page)
    login.open("/")
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.should_be_opened()
    inv.add_item(ITEM)
    assert inv.cart_count() == 1

    inv.open_cart()
    CartPage(page).should_have_item(ITEM)


@pytest.mark.smoke
def test_remove_from_cart(page):
    login = LoginPage(page)
    login.open("/")
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.add_item(ITEM)
    inv.open_cart()

    cart = CartPage(page)
    cart.should_have_item(ITEM)
    cart.remove_item(ITEM)
    cart.should_not_have_item(ITEM)
