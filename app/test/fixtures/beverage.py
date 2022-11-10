import pytest
from app.utils.functions import (get_random_price, get_random_string,
                                 LIST_RANGE_5, LIST_RANGE_10)


def beverage_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price()
    }


@pytest.fixture
def beverage_uri():
    return '/beverage/'


@pytest.fixture
def beverage():
    return beverage_mock()


@pytest.fixture
def beverages():
    return [beverage_mock() for _ in range(LIST_RANGE_5)]


@pytest.fixture
def create_beverage(client, beverage_uri) -> dict:
    response = client.post(beverage_uri, json=beverage_mock())
    return response


@pytest.fixture
def create_beverages(client, beverage_uri) -> list:
    beverages = []
    for _ in range(LIST_RANGE_10):
        new_beverage = client.post(beverage_uri, json=beverage_mock())
        beverages.append(new_beverage.json)
    return beverages
