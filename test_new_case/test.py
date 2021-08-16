import yaml


def test():
    data = [1, 3]
    with open("./data_yaml.yml", "w") as f:
        yaml.dump(data, stream=f)