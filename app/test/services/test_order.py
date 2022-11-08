import pytest

def test_create_order_service(create_order):
    created_order = create_order.json
    pytest.assume(create_order.status.startswith('200'))
    pytest.assume(created_order['_id'])
    pytest.assume(created_order['client_address'])
    pytest.assume(created_order['client_dni'])
    pytest.assume(created_order['client_name'])
    pytest.assume(created_order['client_phone'])
    pytest.assume(created_order['ingredient_detail'])
    pytest.assume(created_order['beverage_detail'])
    pytest.assume(created_order['size'])


def test_get_order_by_id_service(client, create_order, order_uri):
    current_order = create_order.json
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in current_order.items():
        pytest.assume(returned_order[param] == value)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order['_id'] in returned_orders)
