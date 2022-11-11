import pytest
from app.utils.functions import (get_random_address, get_random_dni,
                                 get_random_name, get_random_phone,
                                 shuffle_list, LIST_RANGE_10)


def client_data_mock() -> dict:
    return {
        'client_address': get_random_address(),
        'client_dni': get_random_dni(),
        'client_name': get_random_name(),
        'client_phone': get_random_phone()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def create_order(client, order_uri, create_ingredients, create_beverages, create_size) -> list:
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
def create_orders(client, order_uri, create_ingredients, create_beverages, create_sizes) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    sizes = [size.get('_id') for size in create_sizes]
    orders = []
    for _ in range(LIST_RANGE_10):
        new_order = client.post(order_uri, json={
            **client_data_mock(),
            'ingredients': shuffle_list(ingredients)[:5],
            'beverages': shuffle_list(beverages)[:5],
            'size_id': shuffle_list(sizes)[0]
        })
        orders.append(new_order.json)
    return orders
