import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.menu(source_path)

    def menu(self, source_path):
        def read_csv(source_path):
            with open(source_path) as file:
                csv_file = csv.DictReader(file)
                return list(csv_file)
        menu_data = read_csv(source_path)
        foods = {}

        for row in (menu_data):
            name = row['dish']
            price = float(row['price'])
            ingredient_name = row['ingredient']
            new_ingredient = Ingredient(ingredient_name)
            quantity = float(row['recipe_amount'])

            if name not in foods:
                foods[name] = Dish(name, price)

            foods[name].add_ingredient_dependency(new_ingredient, quantity)
        return set(foods.values())

# referencia chatGPT
