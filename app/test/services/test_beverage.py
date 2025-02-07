import pytest
from app.utils.functions import (get_random_price,
                                 get_random_string,
                                 OK_STATUS)


def test_create_beverage_service_returns_created_beverage_when_calls_post_method(create_beverage):
    beverage = create_beverage.json
    pytest.assume(create_beverage.status.startswith(OK_STATUS))
    pytest.assume(beverage['_id'])
    pytest.assume(beverage['name'])
    pytest.assume(beverage['price'])


def test_update_beverage_service_returns_updated_beverage_when_calls_put_method(client, create_beverage, beverage_uri):
    current_beverage = create_beverage.json
    update_data = {**current_beverage,
                   'name': get_random_string(),
                   'price': get_random_price()}
    response = client.put(beverage_uri, json=update_data)
    pytest.assume(response.status.startswith(OK_STATUS))
    updated_beverage = response.json
    for param, value in update_data.items():
        pytest.assume(updated_beverage[param] == value)


def test_get_beverage_by_id_service_returns_a_beverage_when_calls_get_method_with_id(client, create_beverage, beverage_uri):
    current_beverage = create_beverage.json
    response = client.get(f'{beverage_uri}id/{current_beverage["_id"]}')
    pytest.assume(response.status.startswith(OK_STATUS))
    returned_beverage = response.json
    for param, value in current_beverage.items():
        pytest.assume(returned_beverage[param] == value)


def test_get_beverages_service_returns_a_beverage_list_when_calls_get_method(client, create_beverages, beverage_uri):
    response = client.get(beverage_uri)
    pytest.assume(response.status.startswith(OK_STATUS))
    returned_beverages = {beverage['_id']: beverage for beverage in response.json}
    for beverage in create_beverages:
        pytest.assume(beverage['_id'] in returned_beverages)
