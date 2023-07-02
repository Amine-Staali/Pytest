from shoppingCart import *
from item_db import *
from unittest.mock import Mock
import pytest

"""this is a way to define a variable that you're gonna use it inside all the functions"""
@pytest.fixture
def cart():
    return shoppingCart(5)

#test class
class TestClassShoppingCart:
    def test_can_add_item(self, cart):
        cart.add("apple")
        assert cart.size() == 1 #check if the statement is true

    def test_when_item_added_than_cart_contains_item(self, cart):
        cart.add("apple")
        assert "apple" in cart.getItems()
    
    def test_when_add_more_than_max_items(self, cart):
        for _ in range(5):
            cart.add("apple")
        with pytest.raises(OverflowError): #the test passes when the exception is raised
            cart.add("apple")

    def test_can_get_total_price(self, cart):
        cart.add("apple")
        cart.add("orange")
        price_map = ItemDB()
        #price_map.get = Mock(return_value=2.5)
        def mock_get_item(item:str):
            if item == "apple":
                return 3.0
            elif item == "orange":
                return 2.0
        price_map.get = Mock(side_effect = mock_get_item)

        assert cart.getTotalPrice(price_map) == 5.0