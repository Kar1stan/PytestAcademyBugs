from playwright.sync_api import Page

class LatestNewsPage:
    def __init__(self, page: Page):
        self.page = page
        self.play_button1 = page.locator("div[class='plyr__controls']>button[aria-label='Play']").first
        self.play_button2 = page.locator("div[class='plyr__controls']>button[aria-label='Play']").nth(2)
        # The first play button is located using .first because there are multiple play buttons on the page and we want to select the first one,
        # The second play button is located using .nth(2) - it's third one in the list of play buttons because the index starts from 0, so .nth(2) will select the third play button.
      

    def click_play_button1(self):
        self.play_button1.click()

    def click_play_button2(self):
        self.play_button2.click()