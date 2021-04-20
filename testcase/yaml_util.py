import yaml
import requests
class YamlUtil:
    def __init__(self,yaml_file):
        """
        通过init方法把yaml文件传入这个类
        """
        self.yaml_file = yaml_file
    #读取yaml文件
    def read_yaml(self):
        """
        读取yaml，对yaml反序列化，将yaml格式转化为dict格式
        :return:
        """
        with open(self.yaml_file,encoding='utf-8') as f:
            value = yaml.load(f,Loader=yaml.Loader)
            return value

if __name__ == '__main__':
    YamlUtil('test_api.yaml').read_yaml()