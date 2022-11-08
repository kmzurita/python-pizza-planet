import pytest
from faker import Faker

fake = Faker()


def size_mock() -> dict:
    return {
        'name': fake.pystr(),
        'price': fake.pyfloat(left_digits=2, right_digits=3, positive=True)
    }


@pytest.fixture
def size_uri():
    return '/size/'


@pytest.fixture
def size():
    return size_mock()


@pytest.fixture
def sizes():
    return [size_mock() for _ in range(5)]


@pytest.fixture
def create_size(client, size_uri) -> dict:
    response = client.post(size_uri, json=size_mock())
    return response


@pytest.fixture
def create_sizes(client, size_uri) -> list:
    sizes = []
    for _ in range(10):
        new_size = client.post(size_uri, json=size_mock())
        sizes.append(new_size.json)
    return sizes
