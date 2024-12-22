import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database

@pytest.fixture()
def create_new_bun():
    new_bun = Bun("black bun", 100)
    return new_bun

@pytest.fixture()
def create_new_ingredient():
    new_ingredient = Ingredient('SAUCE', "hot sauce", 100)
    return new_ingredient

@pytest.fixture()
def create_new_database():
    new_database = Database()
    return new_database