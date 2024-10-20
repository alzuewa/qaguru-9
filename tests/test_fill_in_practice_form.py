from models.data import user_data
from pages.registration_form_page import RegistrationPage


def test_fill_in_practice_form(driver):
    registration_page = RegistrationPage()
    user = user_data.test_user

    registration_page.open_form()
    registration_page.register_user(user)
    registration_page.should_have_registered_user_with_data(user)
