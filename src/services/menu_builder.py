import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        dishes = self.menu_data.dishes
        menu_restrictions = list()

        for dish in dishes:
            restrictions_dish = dish.get_restrictions()
            if restriction not in restrictions_dish:
                newDish = {
                    "dish_name": dish.name,
                    "price": dish.price,
                    "ingredients": dish.get_ingredients(),
                    "restrictions": restrictions_dish
                }
                menu_restrictions.append(newDish)
        return pd.DataFrame(menu_restrictions)
