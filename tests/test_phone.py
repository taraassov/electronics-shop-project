from src.item import Item
from src.phone import Phone

def test_str():
    phone1 = Phone("nokia 3310", 10000, 4, 1)
    assert str(phone1) == 'nokia 3310'

def test_repr_sim():
    phone1 = Phone("nokia 3310", 10000, 4, 1)
    assert repr(phone1) == "Phone('nokia 3310', 10000, 4, 1)"

    assert phone1.number_of_sim == 1

def test_addition():
    phone1 = Phone("nokia 3310", 10000, 4, 1)
    item1 = Item("simens a35", 8000, 6)
    assert phone1 + item1 == 10
    assert phone1 + phone1 == 8

