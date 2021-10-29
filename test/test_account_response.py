"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

import ynab_api
from ynab_api.model.account_response_data import AccountResponseData

globals()['AccountResponseData'] = AccountResponseData
from ynab_api.model.account_response import AccountResponse


class TestAccountResponse(unittest.TestCase):
    """AccountResponse unit test stubs"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountResponse(self):
        """Test AccountResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
