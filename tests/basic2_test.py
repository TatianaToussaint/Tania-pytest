import pytest


def test_another_login():
    print("another login")


@pytest.mark.skip
def test_another_navigation():
    print("another_navigation")


@pytest.mark.smoke
def test_another_logout():
    print("another_logout")
