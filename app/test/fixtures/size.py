import pytest
from app.utils.functions import (get_random_price, get_random_string,
                                 LIST_RANGE_5, LIST_RANGE_10)


def size_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price()
    }


@pytest.fixture
def size_uri():
    return '/size/'


@pytest.fixture
def size():
    return size_mock()


@pytest.fixture
def sizes():
    return [size_mock() for _ in range(LIST_RANGE_5)]


@pytest.fixture
def create_size(client, size_uri) -> dict:
    response = client.post(size_uri, json=size_mock())
    return response


@pytest.fixture
def create_sizes(client, size_uri) -> list:
    sizes = []
    for _ in range(LIST_RANGE_10):
        new_size = client.post(size_uri, json=size_mock())
        sizes.append(new_size.json)
    return sizes
