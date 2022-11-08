import pytest
from faker import Faker

from ...utils.functions import (shuffle_list)


fake = Faker()

def client_data_mock() -> dict:
    return {
        'client_address': fake.street_address(),
        'client_dni': str(fake.random_number(digits=10)),
        'client_name': fake.name(),
        'client_phone': fake.phone_number()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def order(create_ingredients, create_beverages, create_size, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.get('_id')
    return client_data_mock() | {
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


@pytest.fixture
def create_order(client, order_uri, create_ingredients, create_beverages, create_size, client_data) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size = create_size.json
    size_id = size.get('_id')
    response = client.post(order_uri, json={
        **client_data_mock(),
        'ingredients': shuffle_list(ingredients)[:5],
        'beverages': shuffle_list(beverages)[:5],
        'size_id': size_id
    })
    return response


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_beverages, create_sizes, client_data) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    sizes = [size.get('_id') for size in create_sizes]
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json={
            **client_data_mock(),
            'ingredients': shuffle_list(ingredients)[:5],
            'beverages': shuffle_list(beverages)[:5],
            'size_id': shuffle_list(sizes)[0]
        })
        orders.append(new_order.json)
    return orders
