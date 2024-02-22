import pytest
from qaseio.pytest import qase
from pages.page_main import PageMain


@pytest.mark.prod
@qase.layer("e2e")
class TestShop:

    @qase.id(0)
    @qase.title("Open Deal card from slider")
    @qase.description("Open Shared charter or Empty leg from Featured Private Jet Flights slider")
    @qase.severity("normal")
    def test_shop(self, page_logged_out, base_url):
        main = PageMain(page_logged_out)

        page_logged_out.goto(base_url)

        with qase.step("Step 1. Click Shop menu", "Shop page opened"):
            main.menu_shop_click()