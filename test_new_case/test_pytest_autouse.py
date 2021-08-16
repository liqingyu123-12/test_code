import pytest


@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")


def test01():
    print("这是test01方法测试")
    raise NameError
    pass


def test02():
    print("这是test02方法测试")
    raise NameError
    pass


if __name__ == '__main__':
    pytest.main(['-vs'])