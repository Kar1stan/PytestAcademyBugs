from playwright.sync_api import Page


class TestHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.send_button = page.locator("//h5[text()='Send button returns an error page']")
        self.articles_button = page.locator("//h5[text()='Articles show an error page'][1]")
        self.send_description = page.locator("//p[text()='Users should be able to send a message when clicking Send, but in this example the button returns an error page.']")
        self.player_description = page.locator("//p[text()='Video players should quickly buffer and play video files, but in this example some videos can’t be played.']")
        self.articles_description = page.locator("//p[text()='The articles should show appropriate content, but in this example clicking an article shows an error page.']")
        self.contact_us_link = page.locator("a[href='https://academybugs.com/contact-us-form/?pid=4434']")
        self.latest_news_link = page.locator("a[href='https://academybugs.com/latest-news/?pid=4434']")
        self.articles_link = page.locator("a[href='https://academybugs.com/articles/?pid=4434']")
        self.videoplayer_button = page.locator("//h5[text()='Video player doesn’t work'][1]")
        # The [1] at the end of the locator is used to select only the first element that matches the locator.

    def click_send_button(self):
        self.send_button.click()

    def click_contact_us_link(self):
        self.contact_us_link.click()

    def click_articles_button(self):
        self.articles_button.click()

    def click_articles_link(self):
        self.articles_link.click()

    def click_latest_news_link(self):
        self.latest_news_link.click()

    def click_videoplayer_button(self):
        self.videoplayer_button.click()
