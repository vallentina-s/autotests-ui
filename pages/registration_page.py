from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.login_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email: str, login: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.login_input.fill(login)
        expect(self.login_input).to_have_value(login)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()
