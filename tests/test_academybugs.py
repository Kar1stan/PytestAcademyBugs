import re
import pytest
from playwright.sync_api import Page, expect
from pages.articles_page import ArticlesPage
from pages.latest_news_page import LatestNewsPage
from utils.test_data import Data
from pages.home_page import TestHomePage
from pages.contact_us_page import ContactUsPage
from utils.tools import take_screenshot



class TestAcademyBugs:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.homepage = TestHomePage(self.page)
        # self is used when you need reuse the same variable and it's methods in multiple test cases inside the test class instance in this case TestAcademyBugs, 
        # so you don't have to create a new variable for each test case, you can just use self.variable_name to access it in any new test case.
        # contact_page on the other hand doesn't need to be reused so we can just create it in the test case itself without using self.

    def test_send_button(self, test_before_each, page: Page):
        """Should verify send button returns an error page"""
        expect(self.page).to_have_url('https://academybugs.com/#')
        self.homepage.click_send_button()
        expect(self.homepage.send_description).to_be_visible()
        with self.page.expect_popup() as popup_info:  
          self.homepage.click_contact_us_link()
        send_page = popup_info.value
        contact_page = ContactUsPage(send_page)
        # The click on the link above opens a new page, so we need to switch to it before making assertions
        # So we're using popup_info.value to get the new page that was opened and then we can make assertions on it
        # contaact_page is needed to be able to use the methods of the ContactUsPage class on the new page that was opened,
        # Otherwise we would make assertions on the original page.
        expect(send_page).to_have_url(re.compile(r"contact-us-form"))
        # re.compile is used to match the URL that contains "contact-us-form" in it, not the whole URL, because the URL might have some dynamic parts that we don't want to assert on.
        
        contact_page.fill_firstname_input(Data.firstname)
        expect(contact_page.firstname_input).to_have_value(Data.firstname)
        contact_page.fill_lastname_input(Data.lastname)
        expect(contact_page.lastname_input).to_have_value(Data.lastname)
        contact_page.fill_email_input(Data.email)
        expect(contact_page.email_input).to_have_value(Data.email)
        contact_page.fill_subject_input(Data.subject)
        expect(contact_page.subject_input).to_have_value(Data.subject)
        contact_page.fill_message_input(Data.message)
        expect(contact_page.message_input).to_have_value(Data.message)
        contact_page.click_submit_button()
        expect(contact_page.error_message).to_be_visible()
        take_screenshot(send_page, "test1: Contact Us form error message")

    def test_videoplayer_button(self, test_before_each, page: Page):
        """Should verify video player button returns an error page"""
        expect(self.page).to_have_url('https://academybugs.com/#')
        self.homepage.click_videoplayer_button()
        expect(self.homepage.player_description).to_be_visible()
        with self.page.expect_popup() as popup_info: 
          self.homepage.click_latest_news_link()
        video_page = popup_info.value
        news_page = LatestNewsPage(video_page)
        # Doing the same as in the previous test case, switching to the new page that was opened and creating an instance of the LatestNewsPage class to be able to use its methods on the new page.
        
        expect(video_page).to_have_url(re.compile(r"latest-news"))
        news_page.click_play_button1()
        news_page.click_play_button2()
        take_screenshot(video_page, "test2: Latest News page with video player")

    def test_articles_button(self, test_before_each, page: Page):
        """Should verify articles show an error page"""
        expect(self.page).to_have_url('https://academybugs.com/#')
        self.homepage.click_articles_button()
        expect(self.homepage.articles_description).to_be_visible()
        with self.page.expect_popup() as popup_info: 
          self.homepage.click_articles_link()
        articles_page = popup_info.value
        article_page = ArticlesPage(articles_page)
        # Doing the same as in the previous test cases, switching to the new page that was opened and creating an instance of the ArticlesPage class to be able to use its methods on the new page.

        expect(articles_page).to_have_url(re.compile(r"articles"))
        article_page.click_read_more_button()
        expect(article_page.error_page).to_be_visible()
        take_screenshot(articles_page, "test3: Articles page with error message")

        
       
        

