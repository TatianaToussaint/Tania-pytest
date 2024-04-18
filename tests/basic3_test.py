import pytest


def test_new_login():
    print("new login")


@pytest.mark.regression
def test_new_navigation():
    print("new navigation")


@pytest.mark.smoke
def test_new_logout():
    print("new logout")
