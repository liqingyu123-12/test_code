import pytest


def test01(login):
    print("这是test01方法测试")
    a = "sdfa"
    b = "sdfad"
    assert a in b


def test02():
    print("这是test02方法测试")
    assert 1 == 2


def test03(login):
    print("这是test03方法测试")
    assert 2 == 2


if __name__ == '__main__':
    pytest.main(['-vs'])