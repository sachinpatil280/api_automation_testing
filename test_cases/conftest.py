import pytest
from utilities.read_properties import read_config
from utilities.request import APIRequest


@pytest.fixture
def api_instance():
    request = APIRequest()
    request.base_uri = read_config('URI')['base_uri']
    return request
