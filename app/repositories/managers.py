from typing import Any, List, Optional, Sequence
from collections import Counter

from sqlalchemy.sql import text, column

from .models import Ingredient, Order, IngredientOrderDetail, BeverageOrderDetail, Size, Beverage, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
            (IngredientOrderDetail(
                order_id=new_order._id,
                ingredient_id=ingredient._id,
                ingredient_price=ingredient.price)
             for ingredient in ingredients))
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
            (BeverageOrderDetail(
                order_id=new_order._id,
                beverage_id=beverage._id,
                beverage_price=beverage.price)
             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class ReportManager(BaseManager):
    order_model = Order
    ingredient_order_detail_model = IngredientOrderDetail
    session = db.session

    @classmethod
    def get_most_request_ingredient(cls):
        ingredient_order_detail_list = cls.session.query(
            cls.ingredient_order_detail_model).all()
        ingredients_id_list = [ingredient_order_detail.ingredient_id
                               for ingredient_order_detail
                               in ingredient_order_detail_list]
        if ingredients_id_list:
            ingredients_count = Counter(ingredients_id_list)
            for id, count in ingredients_count.most_common(1):
                ingredient_id = id
                ingredient_count = count
            most_requested_ingredient = Ingredient.query.get(ingredient_id)
            return {
                'name': most_requested_ingredient.name,
                'count': ingredient_count
            }

    @classmethod
    def get_month_with_most_revenue(cls) -> dict:
        order_list = cls.session.query(cls.order_model).all()
        date_list = [(order.date.month, order.total_price)
                     for order in order_list]
        if date_list:
            monthly_revenue_report = {month: 0 for month, _ in date_list}
            for month_of_order, total_price in date_list:
                monthly_revenue_report.update(
                    {month_of_order: total_price + monthly_revenue_report.get(month_of_order)})
            sorted_report = sorted(
                monthly_revenue_report.items(),
                key=lambda x: x[1],
                reverse=True)
            return {
                'month': sorted_report[0][0],
                'revenue': round(sorted_report[0][1], 2)
            }

    @classmethod
    def get_best_customers(cls) -> dict:
        order_list = cls.session.query(cls.order_model).all()
        client_data = [client.client_dni for client in order_list]
        if client_data:
            clients_count = Counter(client_data)
            most_loyal_customers = clients_count.most_common(3)
            return {
                'customers': [
                    {
                        'dni': dni,
                        'name': cls.get_client_name(dni, order_list),
                        'number_of_purchases': number_of_purchases
                    } for dni, number_of_purchases in most_loyal_customers
                ]
            }

    @staticmethod
    def get_client_name(dni: str, order_list: list) -> str:
        for order in order_list:
            if order.client_dni == dni:
                return order.client_name


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
