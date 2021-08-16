import pytest

def setup_module():
    print("这是setup_module方法")


def teardown_module():
    print("这是teardown_module方法")


def setup_function():
    print("这是setup_function方法")


def teardown_function():
    print("这是teardown_function方法")


def test_login():
    print("这是一个外部的方法")


class Testcase():
    def setup_class(self):
        print("这是setup_class方法")

    def setup_method(self):
        print("这是setup_method方法")

    def setup(self):
        print("这是setup方法")

    def teardown_method(self):
        print("这是teardown_method方法")

    def teardown_class(self):
        print("这是teardown_class方法")

    def teardown(self):
        print("这是teardown方法")

    def test01(self):
        print("开始执行方法1")
        a = "sdfsa"
        b = "sdfsa"
        assert a not in b

    def test02(self):
        print("开始执行方法2")
        a = "sdf"
        b = "sdfsa"
        assert a in b


if __name__ == '__main__':
    pytest.main(['-vs'])
