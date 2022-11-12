import pytest
from app.utils.functions import (get_random_price,
                                 get_random_string,
                                 OK_STATUS)


def test_create_ingredient_service_returns_created_ingredient_when_calls_post_method(create_ingredient):
    ingredient = create_ingredient.json
    pytest.assume(create_ingredient.status.startswith(OK_STATUS))
    pytest.assume(ingredient['_id'])
    pytest.assume(ingredient['name'])
    pytest.assume(ingredient['price'])


def test_update_ingredient_service_returns_updated_ingredient_when_calls_put_method(client, create_ingredient, ingredient_uri):
    current_ingredient = create_ingredient.json
    update_data = {**current_ingredient,
                   'name': get_random_string(),
                   'price': get_random_price()}
    response = client.put(ingredient_uri, json=update_data)
    pytest.assume(response.status.startswith(OK_STATUS))
    updated_ingredient = response.json
    for param, value in update_data.items():
        pytest.assume(updated_ingredient[param] == value)


def test_get_ingredient_by_id_service_returns_a_ingredient_when_calls_get_method_with_id(client, create_ingredient, ingredient_uri):
    current_ingredient = create_ingredient.json
    response = client.get(f'{ingredient_uri}id/{current_ingredient["_id"]}')
    pytest.assume(response.status.startswith(OK_STATUS))
    returned_ingredient = response.json
    for param, value in current_ingredient.items():
        pytest.assume(returned_ingredient[param] == value)


def test_get_ingredients_service_returns_a_ingredient_list_when_calls_get_method(client, create_ingredients, ingredient_uri):
    response = client.get(ingredient_uri)
    pytest.assume(response.status.startswith(OK_STATUS))
    returned_ingredients = {
        ingredient['_id']: ingredient for ingredient in response.json}
    for ingredient in create_ingredients:
        pytest.assume(ingredient['_id'] in returned_ingredients)
