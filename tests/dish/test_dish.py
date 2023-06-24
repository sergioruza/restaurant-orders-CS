import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient


def test_dish():
    mostarda = Dish('Mostarda', 10.50)
    mostarda2 = Dish('Mostarda', 10.50)
    costelao_brabissimo = Dish('Costela', 25.99)
    mostarda.add_ingredient_dependency(Ingredient('Curcuma'), 6)
    ingredients_food = mostarda.get_ingredients()

    assert costelao_brabissimo.name == 'Costela'
    assert mostarda == mostarda2
    assert hash(mostarda) == hash(mostarda2)
    assert repr(costelao_brabissimo) == "Dish('Costela', R$25.99)"
    assert costelao_brabissimo.get_restrictions() == set()
    assert hash(costelao_brabissimo) != hash(mostarda2)
    assert ingredients_food == {Ingredient('Curcuma')}

    with pytest.raises(TypeError):
        Dish('costela', '25.99')

    with pytest.raises(ValueError):
        Dish('costela', -25.99)
