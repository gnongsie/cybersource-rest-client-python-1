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
from CyberSource.apis.report_definitions_api import ReportDefinitionsApi


class TestReportDefinitionsApi(unittest.TestCase):
    """ ReportDefinitionsApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.report_definitions_api.ReportDefinitionsApi()

    def tearDown(self):
        pass

    def test_get_resource_info_by_report_definition(self):
        """
        Test case for get_resource_info_by_report_definition

        Get a single report definition information
        """
        pass

    def test_get_resource_v2_info(self):
        """
        Test case for get_resource_v2_info

        Get reporting resource information
        """
        pass


if __name__ == '__main__':
    unittest.main()
