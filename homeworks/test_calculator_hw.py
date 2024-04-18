import pytest
from source.Calculator import Calculator
from utils.file_utils import get_rows


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize("op1, sign, op2, exp", get_rows("homeworks/calculator.csv"))
def test_calculator(op1, sign, op2, exp, calc):
    calc.add(op1)
    if sign == '+':
        calc.add(op2)
    elif sign == '\\':
        calc.divide(op2)
    elif sign == '*':
        calc.multiply(op2)
    elif sign == '-':
        calc.subtract(op2)
    else:
        print("Incorrect sing")

    assert calc.result == int(exp)
