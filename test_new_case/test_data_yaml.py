import pytest
import yaml


# class Testdemo:
#     @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("./data_yaml.yml")))
#     def test_demo(self, a, b):
#         print("两数之和为：", a+b)

class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./data_yaml.yml")))
    def test_01(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print(env["dev"])

    def test(self):
        print(yaml.safe_load(open("./data_yaml.yml")))


if __name__ == "__main__":
    pytest.main(['-vs'])


