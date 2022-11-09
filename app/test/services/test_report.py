import pytest
from faker import Faker

fake = Faker()


def test_get_most_requested_ingredient_service(client, response_uri):
    current_order = create_order.json
    response = client.get(f'{response_uri}ingredient/{current_order["_id"]}')


def test_get_month_with_most_revenue_service(client, response_uri):
    current_order = create_order.json
    response = client.get(f'{response_uri}month/{current_order["_id"]}')


def test_get_best_costumers_service(client, response_uri):
    current_order = create_order.json
    response = client.get(f'{response_uri}costumer/{current_order["_id"]}')
