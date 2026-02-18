import pytest
from ui_e2e.pages.login_page import LoginPage
from ui_e2e.pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.parametrize(
    "username,password,should_pass",
    [
        ("standard_user", "secret_sauce", True),
        ("standard_user", "wrong_pass", False),
    ],
)
def test_login(page, username, password, should_pass):
    login = LoginPage(page)
    login.open("/")
    login.login(username, password)

    if should_pass:
        InventoryPage(page).should_be_opened()
    else:
        login.should_show_error("Username and password do not match")
