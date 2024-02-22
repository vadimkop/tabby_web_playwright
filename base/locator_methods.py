from playwright.sync_api import Page


class Locators:

    def __init__(self, page: Page):
        self.page = page

    def locator(self, selector):
        return self.page.locator(selector)

    def title(self, selector):
        return self.page.get_by_title(selector, exact=True)

    def text(self, selector):
        return self.page.get_by_text(selector, exact=True)

    def alt_text(self, selector):
        return self.page.get_by_alt_text(selector, exact=True)

    def placeholder(self, selector):
        return self.page.get_by_placeholder(selector, exact=True)

    def label(self, selector):
        return self.page.get_by_label(selector, exact=True)

    def test_id(self, selector):
        return self.page.get_by_test_id(selector)

    def role_dialog(self, selector):
        return self.page.get_by_role("dialog", name=selector, exact=True)

    def role_button(self, selector):
        return self.page.get_by_role("button", name=selector, exact=True)

    def role_tab(self, selector):
        return self.page.get_by_role("tab", name=selector, exact=True)

    def role_option(self, selector):
        return self.page.get_by_role("option", name=selector, exact=True)

    def role_link(self, selector):
        return self.page.get_by_role("link", name=selector, exact=True)

    def role_heading(self, selector):
        return self.page.get_by_role("heading", name=selector, exact=True)

    def role_img(self, selector):
        return self.page.get_by_role("img", name=selector, exact=True)

    def role_textbox(self, selector):
        return self.page.get_by_role("textbox", name=selector, exact=True)

    def role_banner_link(self, selector):
        return self.page.get_by_role("banner").get_by_role("link", name=selector, exact=True)

    def role_banner_button(self, selector):
        return self.page.get_by_role("banner").get_by_role("button", name=selector, exact=True)

    def role_dialog_button(self, selector_1, selector_2):
        return self.page.get_by_role("dialog", name=selector_1).get_by_role("button", name=selector_2, exact=True)

    def role_main_text(self, selector):
        return self.page.get_by_role("main").get_by_text(selector, exact=True)

    def role_main_locator(self, selector):
        return self.page.get_by_role("main").locator(selector)
    def role_navigation_link(self, selector_1, selector_2):
        return self.page.get_by_role("navigation", name=selector_1).get_by_role("link", name=selector_2, exact=True)

    def role_contentinfo_link(self, selector):
        return self.page.get_by_role("contentinfo").get_by_role("link", name=selector, exact=True)

    def locator_filter(self, selector_1, selector_2):
        return self.page.locator(selector_1).filter(has_text=selector_2)

    def locator_role_heading(self, selector_1, selector_2):
        return self.page.locator(selector_1).get_by_role("heading", name=selector_2, exact=True)
