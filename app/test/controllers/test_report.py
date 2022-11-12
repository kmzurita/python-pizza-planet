import pytest
from app.controllers import ReportController, OrderController
from app.plugins import db


def test_get_report(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    report, error = ReportController.get_report()
    pytest.assume(error is None)
    pytest.assume(report["month_with_most_revenue"])
    pytest.assume(report["most_requested_ingredient"])
    pytest.assume(report["best_customers"])


def test_get_report_failure(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    db.drop_all()
    report, error = ReportController.get_most_requested_ingredient()
    pytest.assume(report is None)
    pytest.assume(type(error) is str)


def test_get_most_requested_ingredient(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    most_requested_ingredient, error = ReportController.get_most_requested_ingredient()
    pytest.assume(error is None)
    pytest.assume(most_requested_ingredient["name"])
    pytest.assume(most_requested_ingredient["count"])


def test_get_most_requested_ingredient_failure(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    db.drop_all()
    most_requested_ingredient, error = ReportController.get_most_requested_ingredient()
    pytest.assume(most_requested_ingredient is None)
    pytest.assume(type(error) is str)


def test_get_month_with_most_revenue(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    month_with_most_revenue, error = ReportController.get_month_with_most_revenue()
    pytest.assume(error is None)
    pytest.assume(month_with_most_revenue["month"])
    pytest.assume(month_with_most_revenue["revenue"])


def test_get_month_with_most_revenue_failure(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    db.drop_all()
    month_with_most_revenue, error = ReportController.get_month_with_most_revenue()
    pytest.assume(month_with_most_revenue is None)
    pytest.assume(type(error) is str)


def test_get_best_customers(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    best_customers, error = ReportController.get_best_customers()
    pytest.assume(error is None)
    for customer in best_customers:
        pytest.assume(customer["dni"])
        pytest.assume(customer["name"])
        pytest.assume(customer["number_of_purchases"])


def test_get_best_customers_failure(app, create_orders):
    for order in create_orders:
        OrderController.create(order)
    db.drop_all()
    best_customers, error = ReportController.get_best_customers()
    pytest.assume(best_customers is None)
    pytest.assume(type(error) is str)
