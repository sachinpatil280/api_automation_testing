import pytest as pytest
from test_data.data import *


@pytest.mark.regression
def test_sanity_of_api(api_instance):
    '''
    In this test case, we are testing the sanity/health of API by checking if we are receiving 200 as status code.
    assert: assert the status code returned.
    :param api_instance: this is the fixture which returns the wrapper methods for api's get, post and other methods.
    '''
    response = api_instance.get(api_instance.base_uri)
    assert response.status_code == 200


@pytest.mark.regression
def test_date_min_parameter(api_instance):
    '''
    In this test case, we are testing the "date-min" query parameter, and validating the count and length of "data"
    field are correct.
    '''
    response = api_instance.get(f'{api_instance.base_uri}?date-min=now')
    assert response.status_code == 200
    assert len(response.as_dict['data']) == int(response.as_dict['count'])


@pytest.mark.regression
def test_limit_parameter(api_instance):
    '''
    In this test case, we are testing the limit feature and checking the response has the exact number of entries
    defined in query param "limit"
    '''
    response = api_instance.get(f'{api_instance.base_uri}?body=*&limit=3')
    assert len(response.as_dict['data']) == int(response.as_dict['count'])
    assert len(response.as_dict['data']) == 3
    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.parametrize("api_input, api_output", date_min_data)
def test_date_min_with_parameterized_inputs(api_instance, api_input, api_output):
    '''
    In this test case, we are testing in different way, by providing the input and expected status code.
    :param api_instance: this is the fixture which returns the wrapper methods for api's get, post and other methods.
    :param api_input: input data for validating the api's
    :param api_output: expected output for validating api's response.
    '''
    response = api_instance.get(f'{api_instance.base_uri}?date-min={api_input}')
    assert response.status_code == api_output


@pytest.mark.regression
@pytest.mark.parametrize("api_input, api_output_msg, api_output_status_code", spk_data)
def test_spk_with_parameterized_inputs(api_instance, api_input, api_output_msg, api_output_status_code):
    '''
    In this test case, we are testing in different way, by providing the input, message, and expected status code.
    :param api_instance: this is the fixture which returns the wrapper methods for api's get, post and other methods.
    :param api_input: input data for validating the api's
    :param api_output: expected output for validating api's response.
    '''
    response = api_instance.get(f'{api_instance.base_uri}?spk={api_input}')
    assert response.as_dict['message'] == api_output_msg
    assert response.status_code == api_output_status_code
