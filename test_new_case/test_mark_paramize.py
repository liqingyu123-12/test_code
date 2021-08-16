import pytest
import sys

# 参数化，前两个是变量，后面对应的是数值
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7)])
def test_eval(test_input, expected):
    # eval将字符串str当成有限的表达式来求值，并返回结果
    assert eval(test_input) == expected


# 参数组合
@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [5, 6, 8])
def test_foo(a, b):
    print(f"a:{a},b:{b}")


# 方法名做参数
test_user_data = ['tom', 'marry']
@pytest.fixture(scope='module')
def login_r(request):
    # 接收传入的参数
    user = request.param
    print(f"\n 打开首页准备登陆，登陆用户:{user}")
    return user

@pytest.mark.xfail
# @pytest.mark.skip("此测试用例不执行")
# indirect=True可以将传过来的参数当做函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值:{a}")
    assert a != ""
    raise NameError