from playwright.sync_api import Page

class ArticlesPage:
    def __init__(self, page: Page):
        self.page = page
        self.read_more_button = page.locator("a[href='https://academybugs.com/why-do-i-need-financial-consulting-services']").nth(2)
        self.error_page = page.locator("//h3[normalize-space(.)='404 Error']")
        # normalize-space is used to remove any extra spaces from the text, so it will match the text even if there are extra spaces in it.

    def click_read_more_button(self):
        self.read_more_button.click()