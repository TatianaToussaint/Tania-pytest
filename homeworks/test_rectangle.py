import pytest
from source.Rectangle import Rectangle


@pytest.fixture(scope="module")
def rectangle():
    return Rectangle(20, 10)


def test_area(rectangle):
    assert rectangle.area() == 200


def test_perimeter(rectangle):
    assert rectangle.perimeter() == 60
    