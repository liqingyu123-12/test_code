# from python.calc import Calc
# import pytest
# class TestCalc:
#
#     # 初始化
#     def setup(self):
#         self.calc = Calc()
#     def test_add1(self):
#         result = self.calc.add(1, 3)
#         assert 4 == result
#     @pytest.mark.run(order=1)
#     def test_add2(self):
#         result = self.calc.add(-1,-1)
#         assert -2 == result
#     def test_add3(self):
#         result = self.calc.add(1.0,2.0)
#         assert 3.0 == result
#
#     @pytest.mark.run(order=2)
#     @pytest.mark.div
#     def test_div(self):
#         result = self.calc.div(8,2)
#         assert 4 == result
#     def test_div1(self):
#         result = self.calc.div(1,3)
#         assert 0.3333333333333333 == result
#     # def test_div2(self):
#     #     result = self.calc.div(2,0)
#     #     assert "integer division or modulo by zero" == result
#     def test_div2(self):
#         with pytest.raises(ZeroDivisionError) as e:
#             1 / 0
#             assert str(e.value) == "integer division or modulo by zero"
# if __name__ == '__main__':
#     pytest.main(['-vs'])