from selene import browser, have, command, be

from helpers import resources
from helpers.constants import City, Gender, Hobbies, Month, State, Subject


class RegistrationPage:

    @staticmethod
    def open_form():
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @staticmethod
    def set_first_name(value: str):
        browser.element('#firstName').type(value)

    @staticmethod
    def set_last_name(value: str):
        browser.element('#lastName').type(value)

    @staticmethod
    def set_email(value: str):
        browser.element('#userEmail').type(value)

    @staticmethod
    def set_gender(gender: Gender):
        browser.all('[name="gender"]').element_by(have.attribute(name='value', value=gender)).element(
            '../label').click()

    @staticmethod
    def set_phone_number(phone_number: str):
        browser.element('#userNumber').type(phone_number)

    @staticmethod
    def set_birth_date(year: int, month: Month, day: int):
        def adjust_day_repr(day):
            day = str(day).rjust(3, '0')
            return day

        day = adjust_day_repr(day)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--{day}').click()

    @staticmethod
    def set_subjects(subjects: dict[str, Subject]):
        for letter, subject in subjects.items():
            browser.element('#subjectsInput').type(letter)
            browser.element('.subjects-auto-complete__menu-list').element(f'//*[text()="{subject}"]').perform(
                command.js.scroll_into_view).click()

    @staticmethod
    def set_hobbies(*hobbies: Hobbies):
        for value in hobbies:
            browser.element(f'//label[text()="{value}"]').click()

    @staticmethod
    def upload_picture(file_name: str):
        browser.element('#uploadPicture').set_value(resources.get_path(file_name))

    @staticmethod
    def set_current_address(value: str):
        browser.element('#currentAddress').type(value)

    @staticmethod
    def set_state(value: State):
        browser.element('#state').click()
        browser.element(f'//*[text()="{value}"]').click()

    @staticmethod
    def set_city(value: City):
        browser.element('#city').click()
        browser.element(f'//*[text()="{value}"]').click()

    @staticmethod
    def submit_form():
        browser.element('button#submit').click()

    @staticmethod
    def should_have_registered_user_with_data(
            first_name: str,
            last_name: str,
            email: str,
            gender: Gender,
            phone_number: str,
            birth_year: int,
            birth_month: str,
            birth_day: int,
            subjects: list[Subject],
            hobbies: list[Hobbies],
            picture_name: str,
            current_address: str,
            state: State,
            city: City
    ):
        def adjust_birth_day_repr(day):
            day = str(day).rjust(2, '0')
            return day

        birth_day = adjust_birth_day_repr(birth_day)
        browser.element('table').should(be.visible)
        browser.element('//table//td[text()="Student Name"]/../td[2]').should(
            have.exact_text(f'{first_name} {last_name}'))
        browser.element('//table//td[text()="Student Email"]/../td[2]').should(have.exact_text(email))
        browser.element('//table//td[text()="Gender"]/../td[2]').should(have.exact_text(gender))
        browser.element('//table//td[text()="Mobile"]/../td[2]').should(have.exact_text(phone_number))
        browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(
            have.exact_text(f'{birth_day} {birth_month},{birth_year}')
        )
        browser.element('//table//td[text()="Subjects"]/../td[2]').should(have.exact_text(', '.join(subjects)))
        browser.element('//table//td[text()="Hobbies"]/../td[2]').should(have.exact_text(', '.join(hobbies)))
        browser.element('//table//td[text()="Picture"]/../td[2]').should(have.exact_text(picture_name))
        browser.element('//table//td[text()="Address"]/../td[2]').should(have.exact_text(current_address))
        browser.element('//table//td[text()="State and City"]/../td[2]').should(
            have.exact_text(f'{state} {city}'))
