# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.transaction_details_api import TransactionDetailsApi


class TestTransactionDetailsApi(unittest.TestCase):
    """ TransactionDetailsApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.transaction_details_api.TransactionDetailsApi()

    def tearDown(self):
        pass

    def test_get_transaction(self):
        """
        Test case for get_transaction

        Retrieve a Transaction
        """
        pass


if __name__ == '__main__':
    unittest.main()
