import pytest
from app.controllers import ReportController, OrderController


def test_get_most_requested_ingredient(orders: dict):
    created_orders, _ = OrderController.create(orders)
    report_ingredient_from_db, error = ReportController.get_most_requested_ingredient(
        created_orders['_id'])
    pytest.assume(error is None)
    for param, value in created_orders.items():
        pytest.assume(report_ingredient_from_db[param] == value)


def test_get_month_with_most_revenue(orders: dict):
    created_orders, _ = OrderController.create(orders)
    size_from_db, error = ReportController.get_by_id(created_orders['_id'])
    pytest.assume(error is None)
    for param, value in created_size.items():
        pytest.assume(size_from_db[param] == value)


def test_get_best_costumers(orders: dict):
    created_orders, _ = OrderController.create(orders)
    size_from_db, error = ReportController.get_by_id(created_orders['_id'])
    pytest.assume(error is None)
    for param, value in created_orders.items():
        pytest.assume(size_from_db[param] == value)
