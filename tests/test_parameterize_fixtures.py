import pytest


@pytest.fixture(params= ["Chrome", "Firefox","Edge"])
def browser(request):
    return request.param

def test_app1(browser):
    print("tes1", browser)
    
def test_app2(browser):
    print("tes2", browser)