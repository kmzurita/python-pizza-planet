from random import choices, choice, randrange, sample
from .stored_data import beverage_data, ingredient_data, size_data
from app.utils.functions import (get_random_price, get_random_address,
                                 get_random_name, get_random_phone,
                                 get_random_dni, MAX_DECIMAL_DIGITS)


def _client_data_mock() -> dict:
    return {
        'client_address': get_random_address(),
        'client_dni': get_random_dni(),
        'client_name': get_random_name(),
        'client_phone': get_random_phone()
    }


def generate_random_clients_data(number_of_clients: int):
    return [_client_data_mock() for _ in range(number_of_clients)]


def generate_random_ingredient_list():
    return [
        {
            'name': ingredient,
            'price': get_random_price
        } for ingredient in ingredient_data.ingredients]


def generate_random_beverage_list():
    return [
        {
            'name': beverage,
            'price': get_random_price
        } for beverage in beverage_data.beverages]


def generate_random_size_list():
    return [
        {
            'name': size,
            'price': get_random_price
        } for size in size_data.sizes]


def calculate_total_price(ingredients: list, beverages: list, size_price: float):
    ingredients_price = sum(ingredient.get('price')
                            for ingredient in ingredients)
    beverages_price = sum(beverage.get('price') for beverage in beverages)
    total_price = size_price + ingredients_price + beverages_price
    return round(total_price, MAX_DECIMAL_DIGITS)
