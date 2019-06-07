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


class TssV2TransactionsPost201ResponseEmbeddedProcessingInformation(object):
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
        'payment_solution': 'str',
        'business_application_id': 'str'
    }

    attribute_map = {
        'payment_solution': 'paymentSolution',
        'business_application_id': 'businessApplicationId'
    }

    def __init__(self, payment_solution=None, business_application_id=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedProcessingInformation - a model defined in Swagger
        """

        self._payment_solution = None
        self._business_application_id = None

        if payment_solution is not None:
          self.payment_solution = payment_solution
        if business_application_id is not None:
          self.business_application_id = business_application_id

    @property
    def payment_solution(self):
        """
        Gets the payment_solution of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay. 

        :return: The payment_solution of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        :rtype: str
        """
        return self._payment_solution

    @payment_solution.setter
    def payment_solution(self, payment_solution):
        """
        Sets the payment_solution of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay. 

        :param payment_solution: The payment_solution of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        :type: str
        """
        if payment_solution is not None and len(payment_solution) > 12:
            raise ValueError("Invalid value for `payment_solution`, length must be less than or equal to `12`")

        self._payment_solution = payment_solution

    @property
    def business_application_id(self):
        """
        Gets the business_application_id of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        The description for this field is not available.

        :return: The business_application_id of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        :rtype: str
        """
        return self._business_application_id

    @business_application_id.setter
    def business_application_id(self, business_application_id):
        """
        Sets the business_application_id of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        The description for this field is not available.

        :param business_application_id: The business_application_id of this TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.
        :type: str
        """

        self._business_application_id = business_application_id

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
