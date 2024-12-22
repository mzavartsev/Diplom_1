import pytest
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_set_bun_for_burger(self, create_new_bun):
        new_burger = Burger()
        new_burger.set_buns(create_new_bun)
        assert "black bun" in new_burger.get_receipt()

    def test_add_ingredient_for_burger(self, create_new_ingredient):
        ingredients_list = Mock()
        new_burger = Burger()
        new_burger.add_ingredient(create_new_ingredient)
        ingredients_list.get_ingredient_list_len.return_value = 1
        assert ingredients_list.get_ingredient_list_len() == 1

    def test_remove_ingredient_for_burger(self, create_new_bun, create_new_ingredient):
        new_burger = Burger()
        new_burger.set_buns(create_new_bun)
        new_burger.add_ingredient(create_new_ingredient)
        new_burger.remove_ingredient(0)
        assert "hot sauce" not in new_burger.get_receipt()

    def test_move_ingredient_for_burger(self, create_new_ingredient):
        ingredients_list = Mock()
        new_burger = Burger()
        new_burger.add_ingredient(create_new_ingredient)
        create_new_ingredient2 = Ingredient('FILLING', "cutlet", 100)
        new_burger.add_ingredient(create_new_ingredient2)
        ingredients_list.get_ingredient_list.return_value = [create_new_ingredient2, create_new_ingredient]
        new_burger.move_ingredient(0,1)
        assert ingredients_list.get_ingredient_list()[1] == create_new_ingredient