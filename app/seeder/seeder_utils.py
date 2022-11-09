from random import choices, choice, randrange, sample
from faker import Faker
from datetime import datetime, timedelta
from .stored_data import beverage_data, ingredient_data, size_data

_fake = Faker()


def _client_data_mock() -> dict:
    return {
        'client_address': _fake.street_address(),
        'client_dni': str(_fake.random_number(digits=10)),
        'client_name': _fake.name(),
        'client_phone': _fake.phone_number()
    }


def _get_random_price() -> float:
    return _fake.pyfloat(left_digits=1, right_digits=2, positive=True)


def generate_random_clients_data(number_of_clients: int):
    return [_client_data_mock() for _ in range(number_of_clients)]


def generate_random_dates(number_of_orders: int):
    start = datetime.strptime("01-01-2022", "%d-%m-%Y")
    end = datetime.strptime("31-12-2022", "%d-%m-%Y")
    date_generated = [start + timedelta(days=x)
                      for x in range(0, (end-start).days)]
    return choices(date_generated, k=number_of_orders)


def generate_random_ingredient_list():
    return [
        {
            'name': ingredient,
            'price': _get_random_price()
        } for ingredient in ingredient_data.ingredients]


def generate_random_beverage_list():
    return [
        {
            'name': beverage,
            'price': _get_random_price()
        } for beverage in beverage_data.beverages]


def generate_random_size_list():
    return [
        {
            'name': size,
            'price': _get_random_price()
        } for size in size_data.sizes]


def generate_random_list(items: list, range: int):
    return sample(items, k=randrange(range))


def generate_random_choice(items: list):
    return choice(items)


def calculate_total_price(ingredients: list, beverages: list, size_price: float):
    ingredients_price = sum(ingredient.get('price')
                            for ingredient in ingredients)
    beverages_price = sum(beverage.get('price') for beverage in beverages)
    total_price = size_price + ingredients_price + beverages_price
    return round(total_price, 2)
