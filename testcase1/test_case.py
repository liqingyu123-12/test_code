import pytest

def test_02(xuzhu):
    print()

def test_03(xuzhu1):
    assert xuzhu1 == 1,'失败'

if __name__ == '__main__':
    pytest.main(['-s','-rA','test_case.py'])