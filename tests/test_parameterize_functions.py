import pytest


@pytest.mark.parametrize("browser, os", [
    ("Chrome", "Windows 10"),
    ("Firefox", "MacOS"),
    ("Edge", "Windows 11")
])
def test_application(browser, os):
    print("browser =", browser, "OS =", os)

#_________________________________________________
def get_data():
    return [(1,2), (3,4), (5,6)]


@pytest.mark.parametrize("num1, num2", get_data())
def test_ddt(num1, num2):
    print(num1, num2)

#____________________________________________________
sourse = [
    (2, 3, 6),
    (1, 99, 99),
    (3, -4, -12)
]

@pytest.mark.parametrize("op1, op2, expected", sourse)
def test_multiply(op1, op2, expected):
    assert op1 * op2 == expected
    