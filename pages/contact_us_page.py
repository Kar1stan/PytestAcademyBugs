from playwright.sync_api import Page


class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.firstname_input = page.locator("input[id='first_name']")
        self.lastname_input = page.locator("input[name='last_name']")
        self.email_input = page.locator("input[name='email']")
        self.subject_input = page.locator("input[name='subject']")
        self.message_input = page.locator("textarea[id='input-message']")
        self.submit_button = page.locator("button[id='submit-contact-form']")
        self.error_message = page.locator("//p[text()='Oops! Something went wrong.']")


    def fill_firstname_input(self, firstname):
        self.firstname_input.fill(firstname)

    def fill_lastname_input(self, lastname):
        self.lastname_input.fill(lastname)

    def fill_email_input(self, email):
        self.email_input.fill(email)

    def fill_subject_input(self, subject):
        self.subject_input.fill(subject)

    def fill_message_input(self, message):
        self.message_input.fill(message)

    def click_submit_button(self):
        self.submit_button.click()