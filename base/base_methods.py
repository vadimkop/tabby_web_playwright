from playwright.sync_api import Page


class PageMethods:

    def __init__(self, page: Page):
        self.page = page

    def reload_page(self):
        self.page.reload(wait_until="domcontentloaded")

    def wait_load(self):
        self.page.wait_for_load_state()

    def wait_domcontentloaded(self):
        self.page.wait_for_load_state(state="domcontentloaded")

    def switch_page(self, action):
        with self.page.expect_popup() as page_info:
            action()
        return page_info.value

    def close_page(self):
        self.page.close()

    def expect_popup(self):
        self.page.expect_popup()

    def timeout(self, time):
        self.page.wait_for_timeout(time)