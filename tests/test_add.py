import pytest

from source.Calculator import Calculator
from utils.file_utils import get_rows


@pytest.mark.parametrize("op1, op2, exp", get_rows("tests/add.csv"))
def test_add(op1, op2, exp):
    calc = Calculator()
    calc.add(op1)
    calc.add(op2)
    assert calc.result == int(exp)