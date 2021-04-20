import pytest
class TestApi:

    # @pytest.mark.parametrize('name,age',['百丽','李四','王五'])
    @pytest.mark.parametrize('name,age',[['百丽',18],['李四',20]])
    def test_01_baili(self,name,age):
        print(name,age)
if __name__ == '__main__':
    pytest.main(['-vs'])