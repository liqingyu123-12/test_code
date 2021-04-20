import pytest
import yaml

from python.calc import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()

    # @pytest.mark.parametrize("x,y",[
    #     (3+5,8),
    #     (1.0+1.0,2.0),
    #     (-1+(-1),-2)
    # ])
    # @pytest.mark.parametrize("data1,data2,expect",[
    #     (1,2,3),
    #     (1.0,2.0,3.0),
    #     (-1,-2,-3)
    # ])
    @pytest.mark.parametrize("data1,data2,expect",yaml.safe_load(open("data/add.yml")))
    def test_add(self, data1, data2,expect):
        result = self.calc.add(data1,data2)
        assert result == expect

    @pytest.mark.parametrize("data1,data2,expect",[
        (2,1,2),
        (2,0,"integer division or modulo by zero"),
        (1,2,0.5)
    ])
    def test_div(self,data1,data2,expect):
        result = self.calc.div(data1,data2)
        assert result == expect