from playwright.sync_api import Page
from base.locator_methods import Locators
from base.locator_names import LocatorShop
from base.asserts import Asserts
from base.base_methods import PageMethods
import random


class PageShop:

    def __init__(self, page: Page):
        self.page = page

    def assert_shop_opened(self):
        Asserts.url(self, url="/shop")

    def select_product(self):
        products = Locators.locator(self, selector=LocatorShop.PRODUCTS)

        for product in random.sample(products.all(), k=1):
            if product != products.first:
                product.click(force=True)

    def visit_shop_click(self):
        Locators.role_button(self, LocatorShop.VISIT_SHOP_BUTTON).click()

    def reload_page(self):
        PageMethods.reload_page(self)
