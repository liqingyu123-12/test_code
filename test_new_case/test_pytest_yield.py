import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("执行teardown")
    print("最后关闭浏览器")


def test01(open):
    print("这是test01方法测试")
    raise NameError
    pass


def test02(open):
    print("这是test02方法测试")
    raise NameError
    pass


if __name__ == '__main__':
    pytest.main(['-vs'])