from src.models.ingredient import Ingredient


def test_ingredient():
    fettuccine = Ingredient('fettuccine')
    fettuccine2 = Ingredient('fettuccine')
    risoto = Ingredient('risoto')
    assert fettuccine == fettuccine2
    assert fettuccine.restrictions == set()
    assert repr(fettuccine) == "Ingredient('fettuccine')"
    assert risoto.name == 'risoto'
    assert hash(risoto) == hash('risoto')
