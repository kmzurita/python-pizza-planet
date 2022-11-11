import pytest
from app.controllers import ReportController, OrderController


def test_get_most_requested_ingredient(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    most_requested_ingredient, error = ReportController.get_most_requested_ingredient()
    pytest.assume(error is None)
    pytest.assume(most_requested_ingredient["name"])
    pytest.assume(most_requested_ingredient["count"])


def test_get_month_with_most_revenue(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    month_with_most_revenue, error = ReportController.get_month_with_most_revenue()
    print(month_with_most_revenue)
    pytest.assume(error is None)
    pytest.assume(month_with_most_revenue["month"])
    pytest.assume(month_with_most_revenue["revenue"])


def test_get_best_customers(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    best_customers, error = ReportController.get_best_customers()
    print(best_customers)
    pytest.assume(error is None)
    for customer in best_customers:
        pytest.assume(customer["dni"])
        pytest.assume(customer["name"])
        pytest.assume(customer["number_of_purchases"])
        
