import random
from typing import Any, Union
from faker import Faker

_fake = Faker()

MAX_INTEGER_DIGITS = 1
MAX_DECIMAL_DIGITS = 2
POSITIVE_NUMBER = True


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def shuffle_list(choices: list) -> list:
    choice_copy = choices.copy()
    random.shuffle(choice_copy)
    return choice_copy


def get_random_price() -> float:
    return _fake.pyfloat(left_digits=MAX_INTEGER_DIGITS,
                         right_digits=MAX_DECIMAL_DIGITS,
                         positive=POSITIVE_NUMBER)


def get_random_addres() -> str:
    return _fake.street_address()


def get_random_name() -> str:
    return _fake.name()


def get_random_phone() -> str:
    return _fake.phone_number()


def get_random_dni() -> str:
    return str(_fake.random_number(digits=10))
