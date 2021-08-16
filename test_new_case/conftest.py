import pytest
@pytest.fixture()
def login():
    print("用户登录")


def pytest_configure(config):
    marker_list = ["search", "login"]  #标签集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
