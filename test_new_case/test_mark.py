import pytest


@pytest.mark.login
def login1():
    print("test_login1")
    pass


@pytest.mark.search
def login1():
    print("test_login1")
    pass


@pytest.mark.login
def login2():
    print("test_login2")
    pass
