from enum import IntEnum, StrEnum


class Gender(StrEnum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Month(IntEnum):
    JANUARY = 0
    FEBRUARY = 1
    MARCH = 2
    APRIL = 3
    MAY = 4
    JUNE = 5
    JULY = 6
    AUGUST = 7
    SEPTEMBER = 8
    OCTOBER = 9
    NOVEMBER = 10
    DECEMBER = 11


class Subject(StrEnum):
    ACCOUNTING = 'Accounting'
    ARTS = 'Arts'
    BIOLOGY = 'Biology'
    CHEMISTRY = 'Chemistry'
    CIVICS = 'Civics'
    COMMERCE = 'Commerce'
    COMPUTER_SCIENCE = 'Computer Science'
    ENGLISH = 'English'
    HINDI = 'Hindi'
    HISTORY = 'History'
    MATHS = 'Maths'
    PHYSICS = 'Physics'
    SOCIAL_STUDIES = 'Social Studies'


class Hobbies(StrEnum):
    MUSIC = 'Music'
    READING = 'Reading'
    SPORTS = 'Sports'


class State(StrEnum):
    HARYANA = 'Haryana'
    NCR = 'NCR'
    RAJASTHAN = 'Rajasthan'
    UTTAR_PRADESH = 'Uttar Pradesh'


class City(StrEnum):
    AGRA = 'Agra'
    DELHI = 'Delhi'
    GURGAON = 'Gurgaon'
    JAIPUR = 'Jaipur'
    JAISELMER = 'Jaiselmer'
    KARNAL = 'Karnal'
    LUCKNOW = 'Lucknow'
    MERRUT = 'Merrut'
    NOIDA = 'Noida'
    PANIPAT = 'Panipat'
