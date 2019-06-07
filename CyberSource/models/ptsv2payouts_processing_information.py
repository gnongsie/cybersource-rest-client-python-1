# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ptsv2payoutsProcessingInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'business_application_id': 'str',
        'network_routing_order': 'str',
        'commerce_indicator': 'str',
        'reconciliation_id': 'str',
        'payouts_options': 'Ptsv2payoutsProcessingInformationPayoutsOptions'
    }

    attribute_map = {
        'business_application_id': 'businessApplicationId',
        'network_routing_order': 'networkRoutingOrder',
        'commerce_indicator': 'commerceIndicator',
        'reconciliation_id': 'reconciliationId',
        'payouts_options': 'payoutsOptions'
    }

    def __init__(self, business_application_id=None, network_routing_order=None, commerce_indicator=None, reconciliation_id=None, payouts_options=None):
        """
        Ptsv2payoutsProcessingInformation - a model defined in Swagger
        """

        self._business_application_id = None
        self._network_routing_order = None
        self._commerce_indicator = None
        self._reconciliation_id = None
        self._payouts_options = None

        if business_application_id is not None:
          self.business_application_id = business_application_id
        if network_routing_order is not None:
          self.network_routing_order = network_routing_order
        if commerce_indicator is not None:
          self.commerce_indicator = commerce_indicator
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if payouts_options is not None:
          self.payouts_options = payouts_options

    @property
    def business_application_id(self):
        """
        Gets the business_application_id of this Ptsv2payoutsProcessingInformation.
        Payouts transaction type.  Applicable Processors: FDC Compass, Paymentech, CtV  Possible values:  **Credit Card Bill Payment**   - **CP**: credit card bill payment  **Funds Disbursement**   - **FD**: funds disbursement  - **GD**: government disbursement  - **MD**: merchant disbursement  **Money Transfer**   - **AA**: account to account. Sender and receiver are same person.  - **PP**: person to person. Sender and receiver are different.  **Prepaid Load**   - **TU**: top up 

        :return: The business_application_id of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._business_application_id

    @business_application_id.setter
    def business_application_id(self, business_application_id):
        """
        Sets the business_application_id of this Ptsv2payoutsProcessingInformation.
        Payouts transaction type.  Applicable Processors: FDC Compass, Paymentech, CtV  Possible values:  **Credit Card Bill Payment**   - **CP**: credit card bill payment  **Funds Disbursement**   - **FD**: funds disbursement  - **GD**: government disbursement  - **MD**: merchant disbursement  **Money Transfer**   - **AA**: account to account. Sender and receiver are same person.  - **PP**: person to person. Sender and receiver are different.  **Prepaid Load**   - **TU**: top up 

        :param business_application_id: The business_application_id of this Ptsv2payoutsProcessingInformation.
        :type: str
        """
        if business_application_id is not None and len(business_application_id) > 2:
            raise ValueError("Invalid value for `business_application_id`, length must be less than or equal to `2`")

        self._business_application_id = business_application_id

    @property
    def network_routing_order(self):
        """
        Gets the network_routing_order of this Ptsv2payoutsProcessingInformation.
        This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to get the attributes for specified networks only. The networks specified in this field must be a subset of the information provided during program enrollment. Refer to Sharing Group Code/Network Routing Order. Note: Supported only in US for domestic transactions involving Push Payments Gateway Service.  VisaNet checks to determine if there are issuer routing preferences for any of the networks specified by the network routing order. If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on the issuer’s preference.  If an issuer preference exists for more than one of the specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on the acquirer’s routing priorities.   See https://developer.visa.com/request_response_codes#network_id_and_sharing_group_code , under section 'Network ID and Sharing Group Code' on the left panel for available values 

        :return: The network_routing_order of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._network_routing_order

    @network_routing_order.setter
    def network_routing_order(self, network_routing_order):
        """
        Sets the network_routing_order of this Ptsv2payoutsProcessingInformation.
        This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to get the attributes for specified networks only. The networks specified in this field must be a subset of the information provided during program enrollment. Refer to Sharing Group Code/Network Routing Order. Note: Supported only in US for domestic transactions involving Push Payments Gateway Service.  VisaNet checks to determine if there are issuer routing preferences for any of the networks specified by the network routing order. If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on the issuer’s preference.  If an issuer preference exists for more than one of the specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on the acquirer’s routing priorities.   See https://developer.visa.com/request_response_codes#network_id_and_sharing_group_code , under section 'Network ID and Sharing Group Code' on the left panel for available values 

        :param network_routing_order: The network_routing_order of this Ptsv2payoutsProcessingInformation.
        :type: str
        """
        if network_routing_order is not None and len(network_routing_order) > 30:
            raise ValueError("Invalid value for `network_routing_order`, length must be less than or equal to `30`")

        self._network_routing_order = network_routing_order

    @property
    def commerce_indicator(self):
        """
        Gets the commerce_indicator of this Ptsv2payoutsProcessingInformation.
        Type of transaction.  Some payment card companies use this information when determining discount rates. When you omit this field for Ingenico ePayments, the processor uses the default transaction type they have on file for you instead of the default value listed here.  For details, see the `e_commerce_indicator` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  Possible value for Payouts: - internet  #### Ingenico ePayments Ingenico ePayments was previously called _Global Collect_.  #### Payer Authentication Transactions For the possible values and requirements, see \"Payer Authentication\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Other Types of Transactions For details, see \"Commerce Indicators\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The commerce_indicator of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._commerce_indicator

    @commerce_indicator.setter
    def commerce_indicator(self, commerce_indicator):
        """
        Sets the commerce_indicator of this Ptsv2payoutsProcessingInformation.
        Type of transaction.  Some payment card companies use this information when determining discount rates. When you omit this field for Ingenico ePayments, the processor uses the default transaction type they have on file for you instead of the default value listed here.  For details, see the `e_commerce_indicator` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  Possible value for Payouts: - internet  #### Ingenico ePayments Ingenico ePayments was previously called _Global Collect_.  #### Payer Authentication Transactions For the possible values and requirements, see \"Payer Authentication\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Other Types of Transactions For details, see \"Commerce Indicators\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param commerce_indicator: The commerce_indicator of this Ptsv2payoutsProcessingInformation.
        :type: str
        """
        if commerce_indicator is not None and len(commerce_indicator) > 13:
            raise ValueError("Invalid value for `commerce_indicator`, length must be less than or equal to `13`")

        self._commerce_indicator = commerce_indicator

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv2payoutsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :return: The reconciliation_id of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv2payoutsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :param reconciliation_id: The reconciliation_id of this Ptsv2payoutsProcessingInformation.
        :type: str
        """
        if reconciliation_id is not None and len(reconciliation_id) > 60:
            raise ValueError("Invalid value for `reconciliation_id`, length must be less than or equal to `60`")

        self._reconciliation_id = reconciliation_id

    @property
    def payouts_options(self):
        """
        Gets the payouts_options of this Ptsv2payoutsProcessingInformation.

        :return: The payouts_options of this Ptsv2payoutsProcessingInformation.
        :rtype: Ptsv2payoutsProcessingInformationPayoutsOptions
        """
        return self._payouts_options

    @payouts_options.setter
    def payouts_options(self, payouts_options):
        """
        Sets the payouts_options of this Ptsv2payoutsProcessingInformation.

        :param payouts_options: The payouts_options of this Ptsv2payoutsProcessingInformation.
        :type: Ptsv2payoutsProcessingInformationPayoutsOptions
        """

        self._payouts_options = payouts_options

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Ptsv2payoutsProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
