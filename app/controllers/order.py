from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (IngredientManager, OrderManager,
                                     SizeManager, BeverageManager)
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni',
                       'client_address', 'client_phone', 'size_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
        ingredients_price = sum(ingredient.price for ingredient in ingredients)
        beverages_price = sum(beverage.price for beverage in beverages)
        total_price = size_price + beverages_price + ingredients_price
        return round(total_price, 2)

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(_id=size_id)

        beverages_ids = current_order.pop('beverages', [])
        ingredient_ids = current_order.pop('ingredients', [])
        try:
            ingredients = IngredientManager.get_by_id_list(ids=ingredient_ids)
            beverages = BeverageManager.get_by_id_list(ids=beverages_ids)
            price = cls.calculate_order_price(
                size_price=size.get('price'),
                ingredients=ingredients,
                beverages=beverages)
            order_with_price = {**current_order, 'total_price': price}
            return cls.manager.create(order_data=order_with_price,
                                      ingredients=ingredients,
                                      beverages=beverages), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
