import pytest


@pytest.fixture
def sample_string():
    return "Hello, this is a sample string"

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]