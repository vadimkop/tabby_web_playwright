from playwright.sync_api import Page
from base.locator_methods import Locators
from base.locator_names import LocatorShop
from base.asserts import Asserts
import random


class PageShop:

    def __init__(self, page: Page):
        self.page = page

    def assert_shop_opened(self):
        Asserts.url(self, url="/shop")

    def select_product(self):
        products = Locators.locator(self, selector=LocatorShop.PRODUCTS)

        for product in random.sample(products.all(), k=1):
            product.dispatch_event('click')

    def visit_shop_click(self):
        Locators.role_button(self, LocatorShop.VISIT_SHOP_BUTTON).click()
