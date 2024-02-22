from playwright.sync_api import Page
from base.locator_methods import Locators
from base.locator_names import LocatorMenu


class PageMain:

    def __init__(self, page: Page):
        self.page = page

    def menu_shop_click(self):
        Locators.role_link(self, selector=LocatorMenu.MENU_SHOP).click()
