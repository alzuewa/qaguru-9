from dataclasses import dataclass

from helpers.constants import City, Gender, Hobbies, Month, State, Subject


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    birth_year: int
    birth_month: Month
    birth_day: int
    subjects: dict[str, Subject]
    hobbies: list[Hobbies]
    picture_name: str
    current_address: str
    state: State
    city: City
