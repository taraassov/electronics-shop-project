"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
from src.item import Item, InstantiateCSVError
import pytest

def test_item_creation():
    item = Item("Test Item", 10, 5)
    assert item.name == "Test Item"
    assert item.price == 10
    assert item.quantity == 5
    assert Item.all == [item]

def test_calculate_total_price():
    item = Item("Test Item", 10, 5)
    assert item.calculate_total_price() == 50

def test_apply_discount():
    item = Item("Test Item", 10, 5)
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 5
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 4

def test_apply_discount_with_zero_discount():
    item = Item("Test Item", 10, 5)
    item.pay_rate = 0
    item.apply_discount()
    assert item.price == 0

def test_path():
    Item.instantiate_from_csv('src/test1.csv')
    assert len(Item.all) == 9

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item1 = Item("Патифон", 4000, 3)
    assert repr(item1) == "Item('Патифон', 4000, 3)"

def test_str():
    item2 = Item("Патифон", 4000, 3)
    assert str(item2) == 'Патифон'

def test_add():
    item1 = Item("Патифон", 4000, 3)
    item2 = Item("Домофон", 44, 7)
    assert item1 + item2 == 10


def test_instantiate_from_csv():

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('src/test2.csv')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('src/test3.csv')