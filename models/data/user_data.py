from helpers.constants import City, Gender, Hobbies, Month, State, Subject
from models.user import User

test_user = User(
    first_name='Tom',
    last_name='Brown',
    email='tombrown@test.test',
    gender=Gender.MALE,
    phone_number='1234567890',
    birth_year=1970,
    birth_month=Month.SEPTEMBER,
    birth_day=15,
    subjects=dict(e=Subject.ENGLISH, a=Subject.ARTS),
    hobbies=[Hobbies.SPORTS],
    picture_name='image.jpg',
    current_address='Any random place here',
    state=State.UTTAR_PRADESH,
    city=City.LUCKNOW
)
