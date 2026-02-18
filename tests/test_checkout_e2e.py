import pytest
from ui_e2e.pages.login_page import LoginPage
from ui_e2e.pages.inventory_page import InventoryPage
from ui_e2e.pages.cart_page import CartPage
from ui_e2e.pages.checkout_info_page import CheckoutInfoPage
from ui_e2e.pages.checkout_overview_page import CheckoutOverviewPage
from ui_e2e.pages.checkout_complete_page import CheckoutCompletePage


@pytest.mark.smoke
def test_checkout_e2e(page):
    item = "Sauce Labs Backpack"

    # Login
    login = LoginPage(page)
    login.open("/")
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory = InventoryPage(page)
    inventory.should_be_opened()
    inventory.add_item(item)
    assert inventory.cart_count() == 1
    inventory.open_cart()

    # Cart → checkout
    cart = CartPage(page)
    cart.should_have_item(item)
    cart.checkout()

    # Fill info
    info = CheckoutInfoPage(page)
    info.should_be_opened()
    info.fill_and_continue("Dima", "QA", "1010")

    # Overview → finish
    overview = CheckoutOverviewPage(page)
    overview.should_be_opened()
    overview.finish()

    # Complete
    complete = CheckoutCompletePage(page)
    complete.should_be_opened()
    complete.should_show_success()
