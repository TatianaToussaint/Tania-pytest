import pytest


@pytest.fixture()
def setup():
    print("1. Launch browser")
    print("2. Login")
    yield
    print("5. Logout")
    print("6. Close browser")


@pytest.fixture
def number():
    return 8