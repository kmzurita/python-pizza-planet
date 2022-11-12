from app.seeder.seeder_utils import (generate_random_size_list, generate_random_ingredient_list,
                                     generate_random_beverage_list, generate_random_clients_data,
                                     calculate_total_price)
from app.utils.functions import (get_random_choice, get_random_list,
                                 generate_random_dates)
from app.repositories.managers import (
    SizeManager, IngredientManager, BeverageManager, OrderManager)

MAX_NUMBER_OF_DATES = 50
MAX_NUMBER_OF_CLIENTS = 20
MAX_NUMBER_OF_ORDERS = 100
MAX_NUMBER_OF_INGREDIENTS = 10
MAX_NUMBER_OF_BEVERAGES = 10

_sizes = generate_random_size_list()
_ingredients = generate_random_ingredient_list()
_beverages = generate_random_beverage_list()
_dates = generate_random_dates(MAX_NUMBER_OF_DATES)
_clients = generate_random_clients_data(MAX_NUMBER_OF_CLIENTS)


def _seed_size_table(sizes: list):
    if sizes:
        for size in sizes:
            SizeManager.create(size)


def _seed_beverage_table(beverages: list):
    if beverages:
        for beverage in beverages:
            BeverageManager.create(beverage)


def _seed_ingredient_table(ingredients: list):
    if ingredients:
        for ingredient in ingredients:
            IngredientManager.create(ingredient)


def _seed_order_table(dates: list, sizes: list, beverages: list, ingredients: list, clients: list):
    for _ in range(MAX_NUMBER_OF_ORDERS):
        client_data = get_random_choice(clients)
        ordered_size = get_random_choice(sizes)
        ordered_ingredients = get_random_list(
            ingredients,
            MAX_NUMBER_OF_INGREDIENTS)
        ordered_beverages = get_random_list(
            beverages,
            MAX_NUMBER_OF_BEVERAGES)
        total_price = calculate_total_price(
            ordered_ingredients,
            ordered_beverages,
            ordered_size.get('price'))
        order_data = client_data | {
            'date': get_random_choice(dates),
            'size_id': ordered_size.get('_id'),
            'total_price': total_price
        }
        ingredient_list = IngredientManager.get_by_id_list(
            [ingredient.get('_id') for ingredient in ordered_ingredients]
        )
        beverages_list = BeverageManager.get_by_id_list(
            [beverage.get('_id') for beverage in ordered_beverages]
        )
        OrderManager.create(order_data=order_data,
                            ingredients=ingredient_list,
                            beverages=beverages_list)


def seed_database():
    _seed_size_table(sizes=_sizes)
    _seed_ingredient_table(ingredients=_ingredients)
    _seed_beverage_table(beverages=_beverages)
    sizes = SizeManager.get_all()
    ingredients = IngredientManager.get_all()
    beverages = BeverageManager.get_all()
    _seed_order_table(dates=_dates,
                      sizes=sizes,
                      beverages=beverages,
                      ingredients=ingredients,
                      clients=_clients)
