import pytest

def pytest_collection_modifyitems(session,config,items:list):
    for item in items:
        print(item)
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)