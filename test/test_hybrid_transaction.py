"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

import ynab_api
from ynab_api.model.hybrid_transaction_all_of import HybridTransactionAllOf
from ynab_api.model.transaction_summary import TransactionSummary

globals()['HybridTransactionAllOf'] = HybridTransactionAllOf
globals()['TransactionSummary'] = TransactionSummary
from ynab_api.model.hybrid_transaction import HybridTransaction


class TestHybridTransaction(unittest.TestCase):
    """HybridTransaction unit test stubs"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHybridTransaction(self):
        """Test HybridTransaction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HybridTransaction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
