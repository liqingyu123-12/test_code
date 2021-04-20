import yaml


class TestYaml:
    with open("data/add.yml") as f:
       value = yaml.safe_load(f)
       print(value)