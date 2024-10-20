from helpers.constants import City, Gender, Hobbies, Month, State, Subject
from pages.registration_form_page import RegistrationPage


def test_fill_in_practice_form(driver):
    registration_page = RegistrationPage()
    registration_page.open_form()
    registration_page.set_first_name('Tom')
    registration_page.set_last_name('Brown')
    registration_page.set_email('tombrown@test.test')
    registration_page.set_gender(Gender.MALE)
    registration_page.set_phone_number('1234567890')
    registration_page.set_birth_date(year=1970, month=Month.SEPTEMBER, day=15)
    registration_page.set_subjects(dict(e=Subject.ENGLISH, a=Subject.ARTS))
    registration_page.set_hobbies(Hobbies.SPORTS)
    registration_page.upload_picture('image.jpg')
    registration_page.set_current_address('Any random place here')
    registration_page.set_state(State.UTTAR_PRADESH)
    registration_page.set_city(City.LUCKNOW)

    registration_page.submit_form()

    registration_page.should_have_registered_user_with_data(
        first_name='Tom',
        last_name='Brown',
        email='tombrown@test.test',
        gender=Gender.MALE,
        phone_number='1234567890',
        birth_year=1970,
        birth_month='September',
        birth_day=15,
        subjects=[Subject.ENGLISH, Subject.ARTS],
        hobbies=[Hobbies.SPORTS],
        picture_name='image.jpg',
        current_address='Any random place here',
        state=State.UTTAR_PRADESH,
        city=City.LUCKNOW
    )
