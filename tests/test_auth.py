import pytest
from ui_e2e.pages.login_page import LoginPage
from ui_e2e.pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_login_valid(page):
    login = LoginPage(page)
    login.open("/")
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.should_be_opened()


@pytest.mark.smoke
def test_login_invalid(page):
    login = LoginPage(page)
    login.open("/")
    login.login("standard_user", "wrong_pass")
    login.should_show_error("Username and password do not match")
