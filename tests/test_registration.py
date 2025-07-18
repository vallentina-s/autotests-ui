import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize('email, login, password',[('user.name@gmail.com', 'username', 'password'),])

def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email: str, login: str, password: str):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email=email,login=login,password=password)
    registration_page.click_registration_button()
    dashboard_page.dashboard_toolbar_view.check_visible()