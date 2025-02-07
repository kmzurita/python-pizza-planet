import pytest
from app.utils.functions import (get_random_price,
                                 get_random_string,
                                 OK_STATUS)


def test_create_size_service_returns_created_size_when_calls_post_method(create_size):
    size = create_size.json
    pytest.assume(create_size.status.startswith(OK_STATUS))
    pytest.assume(size['_id'])
    pytest.assume(size['name'])
    pytest.assume(size['price'])


def test_update_size_service_returns_updated_size_when_calls_put_method(client, create_size, size_uri):
    current_size = create_size.json
    update_data = {**current_size,
                   'name': get_random_string(),
                   'price': get_random_price()}
    response = client.put(size_uri, json=update_data)
    pytest.assume(response.status.startswith(OK_STATUS))
    updated_size = response.json
    for param, value in update_data.items():
        pytest.assume(updated_size[param] == value)


def test_get_size_by_id_service_returns_a_size_when_calls_get_method_with_id(client, create_size, size_uri):
    current_size = create_size.json
    response = client.get(f'{size_uri}id/{current_size["_id"]}')
    pytest.assume(response.status.startswith(OK_STATUS))
    returned_size = response.json
    for param, value in current_size.items():
        pytest.assume(returned_size[param] == value)


def test_get_sizes_service_returns_a_size_list_when_calls_get_method(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith(OK_STATUS))
    returned_sizes = {size['_id']: size for size in response.json}
    for size in create_sizes:
        pytest.assume(size['_id'] in returned_sizes)
