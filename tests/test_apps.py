import pytest


def testApplication1():
    print("3. Navigation")
    print("4. Test")
    assert True

@pytest.mark.usefixtures("setup")
def testApplication2():
    print("3. Navigation again")
    print("4. Test again")
    assert True