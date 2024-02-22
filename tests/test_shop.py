import pytest
from qaseio.pytest import qase
from pages.page_main import PageMain
from pages.page_shop import PageShop
from pages.page_login import PageLogin


@pytest.mark.prod
@qase.layer("e2e")
class TestShop:

    @qase.id(0)
    @qase.title("Select a product in the shop (Unregistered client) [prod]")
    @qase.description("An unregistered client selects a product in the shop")
    @qase.severity("normal")
    def test_shop_unregistered_client_prod(self, page_logged_out, base_url):
        main = PageMain(page_logged_out)
        shop = PageShop(page_logged_out)
        login = PageLogin(page_logged_out)

        page_logged_out.goto(base_url)

        with qase.step("Step 1. Click Shop menu", "Shop page opened"):
            main.menu_shop_click()
            shop.assert_shop_opened()

        with qase.step("Step 2. Click Split in 4 product", "Split in 4 product opened"):
            shop.reload_page()
            shop.select_product()

        with qase.step("Step 3. Click Visit Shop button", "Enter your phone number popup opened"):
            shop.visit_shop_click()
            login.assert_login_popup()