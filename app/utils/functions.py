import random
from typing import Any, Union
from faker import Faker
from datetime import datetime, timedelta

from app.common.constants import DNI_LENGTH

_fake = Faker()

MAX_INTEGER_DIGITS = 1
MAX_DECIMAL_DIGITS = 2
POSITIVE_NUMBER = True
STARTING_DATE_RANGE = "01-01-2022"
FINISHING_DATE_RANGE = "31-12-2022"
STARTING_RANGE = 0
LIST_RANGE_5 = 5
LIST_RANGE_10 = 10
OK_STATUS = '200'


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def get_random_list(choices: Union[tuple, list], list_range: int) -> Any:
    return random.sample(choices, k=random.randrange(list_range))


def shuffle_list(choices: list) -> list:
    choice_copy = choices.copy()
    random.shuffle(choice_copy)
    return choice_copy


def get_random_price() -> float:
    return _fake.pyfloat(left_digits=MAX_INTEGER_DIGITS,
                         right_digits=MAX_DECIMAL_DIGITS,
                         positive=POSITIVE_NUMBER)


def get_random_address() -> str:
    return _fake.street_address()


def get_random_name() -> str:
    return _fake.name()


def get_random_phone() -> str:
    return _fake.phone_number()


def get_random_dni() -> str:
    return str(_fake.random_number(digits=DNI_LENGTH))


def get_random_string() -> str:
    return _fake.pystr()


def generate_random_dates(number_of_orders: int):
    start = datetime.strptime(STARTING_DATE_RANGE, "%d-%m-%Y")
    end = datetime.strptime(FINISHING_DATE_RANGE, "%d-%m-%Y")
    date_generated = [start + timedelta(days=x)
                      for x in range(STARTING_RANGE, (end-start).days)]
    return random.sample(date_generated, k=number_of_orders)
