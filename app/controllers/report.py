from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import ReportManager


class ReportController():
    manager = ReportManager

    @classmethod
    def get_most_requested_ingredient(cls) -> dict:
        try:
            return cls.manager.get_most_request_ingredient(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_month_with_most_revenue(cls) -> dict:
        try:
            return cls.manager.get_month_with_most_revenue(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_best_customers(cls) -> dict:
        try:
            return cls.manager.get_best_customers(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
