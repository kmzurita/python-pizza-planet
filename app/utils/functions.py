import random
from typing import Any, Union


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def shuffle_list(choices: list) -> list:
    choice_copy = choices.copy()
    random.shuffle(choice_copy)
    return choice_copy
