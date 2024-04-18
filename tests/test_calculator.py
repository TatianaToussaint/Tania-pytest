import pytest

from source.Calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_addition(calc):
    calc.add(9)
    calc.add(1)
    assert calc.result == 10


def test_division(calc):
    calc.add(9)
    calc.divide(3)
    assert calc.result == 3
