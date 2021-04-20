"""
这是pytest中的预置函数（setup和teardown）定义的配置文件(文件名只能是conftest)
scope参数定义的四种等级（默认的等级是function）：
    session：在本次session级别中执行一次
    module：在模块级别中执行一次
    class：在类级别中执行一次
    function：在函数级别中执行，有一个函数就执行一次
"""
import pytest

#预置函数，用于前期的数据准备
@pytest.fixture()
def xuzhu():
    print("牛逼")

@pytest.fixture()
def xuzhu1():
    return 1