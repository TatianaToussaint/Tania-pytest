import pytest


def test_login():
    print("login")
    assert 5 > 3, "5 is greater than 3"


@pytest.mark.regression
def test_navigation():
    print("navigation")


@pytest.mark.smoke
def test_logout():
    print("logout")
