"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

import ynab_api
from ynab_api.model.scheduled_sub_transaction import ScheduledSubTransaction
from ynab_api.model.scheduled_transaction_detail_all_of import ScheduledTransactionDetailAllOf
from ynab_api.model.scheduled_transaction_summary import ScheduledTransactionSummary

globals()['ScheduledSubTransaction'] = ScheduledSubTransaction
globals()['ScheduledTransactionDetailAllOf'] = ScheduledTransactionDetailAllOf
globals()['ScheduledTransactionSummary'] = ScheduledTransactionSummary
from ynab_api.model.scheduled_transaction_detail import ScheduledTransactionDetail


class TestScheduledTransactionDetail(unittest.TestCase):
    """ScheduledTransactionDetail unit test stubs"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScheduledTransactionDetail(self):
        """Test ScheduledTransactionDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScheduledTransactionDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
