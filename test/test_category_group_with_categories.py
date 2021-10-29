"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.category import Category
from openapi_client.model.category_group import CategoryGroup
from openapi_client.model.category_group_with_categories_all_of import CategoryGroupWithCategoriesAllOf
globals()['Category'] = Category
globals()['CategoryGroup'] = CategoryGroup
globals()['CategoryGroupWithCategoriesAllOf'] = CategoryGroupWithCategoriesAllOf
from openapi_client.model.category_group_with_categories import CategoryGroupWithCategories


class TestCategoryGroupWithCategories(unittest.TestCase):
    """CategoryGroupWithCategories unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategoryGroupWithCategories(self):
        """Test CategoryGroupWithCategories"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CategoryGroupWithCategories()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
