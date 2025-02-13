from playwright.sync_api import Page
from base.locator_methods import Locators
from base.locator_names import LocatorLogin
from base.asserts import Asserts
from base.base_methods import PageMethods


class PageLogin:

    def __init__(self, page: Page):
        self.page = page

    def assert_login_popup(self):
        Asserts.visible(self, locator=Locators.test_id(self, selector=LocatorLogin.CONTINUE_LOGIN_BUTTON))
        PageMethods.timeout(self, time=1000)
