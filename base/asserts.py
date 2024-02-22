from playwright.sync_api import expect, Page
import re


class Asserts:

    def __init__(self, page: Page):
        self.page = page

    def attached(self, locator):
        expect(locator).to_be_attached(timeout=20_000)

    def attribute(self, locator, attr, value):
        expect(locator).to_have_attribute(attr, value)

    def visible(self, locator):
        expect(locator).to_be_visible(timeout=60_000)

    def hidden(self, locator):
        expect(locator).to_be_hidden(timeout=20_000)

    def enabled(self, locator):
        expect(locator).to_be_enabled(timeout=20_000)

    def empty(self, locator):
        expect(locator).to_be_empty(timeout=20_000)

    def disabled(self, locator):
        expect(locator).to_be_disabled(timeout=20_000)

    def checked(self, locator):
        expect(locator).to_be_checked(timeout=20_000)

    def not_checked(self, locator):
        expect(locator).not_to_be_checked(timeout=20_000)

    def value(self, locator, value):
        expect(locator).to_have_value(re.compile(value))

    def contain_text(self, locator, value):
        expect(locator).to_contain_text(re.compile(value))

    def locator_or(self, locator_1, locator_2):
        expect(locator_1.or_(locator_2)).to_be_visible()

    def url(self, url):
        expect(self.page).to_have_url(re.compile(url))