"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from ynab_api.api_client import ApiClient, Endpoint as _Endpoint
from ynab_api.model_utils import (  # noqa: F401
    check_allowed_values, check_validations, date, datetime, file_type,
    none_type, validate_and_convert_types)
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.payee_location_response import PayeeLocationResponse
from ynab_api.model.payee_locations_response import PayeeLocationsResponse


class PayeeLocationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_payee_location_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (PayeeLocationResponse, ),
                'auth': ['bearer'],
                'endpoint_path':
                '/budgets/{budget_id}/payee_locations/{payee_location_id}',
                'operation_id': 'get_payee_location_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                    'payee_location_id',
                ],
                'required': [
                    'budget_id',
                    'payee_location_id',
                ],
                'nullable': [],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'budget_id': (str, ),
                    'payee_location_id': (str, ),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                    'payee_location_id': 'payee_location_id',
                },
                'location_map': {
                    'budget_id': 'path',
                    'payee_location_id': 'path',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)
        self.get_payee_locations_endpoint = _Endpoint(
            settings={
                'response_type': (PayeeLocationsResponse, ),
                'auth': ['bearer'],
                'endpoint_path': '/budgets/{budget_id}/payee_locations',
                'operation_id': 'get_payee_locations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                ],
                'required': [
                    'budget_id',
                ],
                'nullable': [],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'budget_id': (str, ),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                },
                'location_map': {
                    'budget_id': 'path',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)
        self.get_payee_locations_by_payee_endpoint = _Endpoint(
            settings={
                'response_type': (PayeeLocationsResponse, ),
                'auth': ['bearer'],
                'endpoint_path':
                '/budgets/{budget_id}/payees/{payee_id}/payee_locations',
                'operation_id': 'get_payee_locations_by_payee',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                    'payee_id',
                ],
                'required': [
                    'budget_id',
                    'payee_id',
                ],
                'nullable': [],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'budget_id': (str, ),
                    'payee_id': (str, ),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                    'payee_id': 'payee_id',
                },
                'location_map': {
                    'budget_id': 'path',
                    'payee_id': 'path',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)

    def get_payee_location_by_id(self, budget_id, payee_location_id, **kwargs):
        """Single payee location  # noqa: E501

        Returns a single payee location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payee_location_by_id(budget_id, payee_location_id, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str): The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
            payee_location_id (str): id of payee location

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PayeeLocationResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        kwargs['payee_location_id'] = \
            payee_location_id
        return self.get_payee_location_by_id_endpoint.call_with_http_info(
            **kwargs)

    def get_payee_locations(self, budget_id, **kwargs):
        """List payee locations  # noqa: E501

        Returns all payee locations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payee_locations(budget_id, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str): The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PayeeLocationsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        return self.get_payee_locations_endpoint.call_with_http_info(**kwargs)

    def get_payee_locations_by_payee(self, budget_id, payee_id, **kwargs):
        """List locations for a payee  # noqa: E501

        Returns all payee locations for a specified payee  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payee_locations_by_payee(budget_id, payee_id, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str): The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
            payee_id (str): id of payee

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PayeeLocationsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        kwargs['payee_id'] = \
            payee_id
        return self.get_payee_locations_by_payee_endpoint.call_with_http_info(
            **kwargs)
