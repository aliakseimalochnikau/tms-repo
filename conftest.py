from random import randint
import pytest


@pytest.fixture(autouse=True)
def age():
    age = randint(0, 100)
    print(f"\nRandom age is {age}")
    yield age


@pytest.fixture(autouse=True)
def delete_age():
    yield
    print("\nDeleting random age... Done")
