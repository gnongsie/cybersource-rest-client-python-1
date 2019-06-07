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


class PaymentInstrumentCard(object):
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
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'issue_number': 'str',
        'start_month': 'str',
        'start_year': 'str',
        'use_as': 'str'
    }

    attribute_map = {
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'issue_number': 'issueNumber',
        'start_month': 'startMonth',
        'start_year': 'startYear',
        'use_as': 'useAs'
    }

    def __init__(self, expiration_month=None, expiration_year=None, type=None, issue_number=None, start_month=None, start_year=None, use_as=None):
        """
        PaymentInstrumentCard - a model defined in Swagger
        """

        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._issue_number = None
        self._start_month = None
        self._start_year = None
        self._use_as = None

        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        self.type = type
        if issue_number is not None:
          self.issue_number = issue_number
        if start_month is not None:
          self.start_month = start_month
        if start_year is not None:
          self.start_year = start_year
        if use_as is not None:
          self.use_as = use_as

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this PaymentInstrumentCard.
        Two-digit month in which the credit card expires. Format: `MM` Possible values: `01` through `12`  This field is optional if your CyberSource account is configured for relaxed requirements for address data and expiration date. For more information about relaxed requirements, see the TMS REST API Developer Guide.  Important: It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :return: The expiration_month of this PaymentInstrumentCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this PaymentInstrumentCard.
        Two-digit month in which the credit card expires. Format: `MM` Possible values: `01` through `12`  This field is optional if your CyberSource account is configured for relaxed requirements for address data and expiration date. For more information about relaxed requirements, see the TMS REST API Developer Guide.  Important: It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :param expiration_month: The expiration_month of this PaymentInstrumentCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")
        if expiration_month is not None and len(expiration_month) < 2:
            raise ValueError("Invalid value for `expiration_month`, length must be greater than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this PaymentInstrumentCard.
        Four-digit year in which the credit card expires. Format: `YYYY`. Possible values: `1900` through `2099`.  **FDC Nashville Global and FDMS South** You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  This field is optional if your CyberSource account is configured for relaxed requirements for address data and expiration date. See Relaxed Requirements for Address Data and Expiration Date page.  Important: It is your responsibility to determine whether a field is required for the transaction you are requesting.' 

        :return: The expiration_year of this PaymentInstrumentCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this PaymentInstrumentCard.
        Four-digit year in which the credit card expires. Format: `YYYY`. Possible values: `1900` through `2099`.  **FDC Nashville Global and FDMS South** You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  This field is optional if your CyberSource account is configured for relaxed requirements for address data and expiration date. See Relaxed Requirements for Address Data and Expiration Date page.  Important: It is your responsibility to determine whether a field is required for the transaction you are requesting.' 

        :param expiration_year: The expiration_year of this PaymentInstrumentCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")
        if expiration_year is not None and len(expiration_year) < 4:
            raise ValueError("Invalid value for `expiration_year`, length must be greater than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this PaymentInstrumentCard.
        Type of credit card. Possible values:   * Visa (001)   * Mastercard (002) - Eurocard—European regional brand of Mastercard   * American Express (003)   * Discover (004)   * Diners Club (005)   * Carte Blanche (006)   * JCB (007)   * Optima (008)   * Twinpay Credit (011)   * Twinpay Debit (012)   * Walmart (013)   * EnRoute (014)   * Lowes consumer (015)   * Home Depot consumer (016)   * MBNA (017)   * Dicks Sportswear (018)   * Casual Corner (019)   * Sears (020)   * JAL (021)   * Disney (023)   * Maestro (024) - UK Domestic   * Sams Club consumer (025)   * Sams Club business (026)   * Nicos (027)   * Bill me later (028)   * Bebe (029)   * Restoration Hardware (030)   * Delta (031) — use this value only for Ingenico ePayments. For other processors, use 001 for all Visa card types.   * Solo (032)   * Visa Electron (033)   * Dankort (034)   * Laser (035)   * Carte Bleue (036) — formerly Cartes Bancaires   * Cartes Bancaires (036)   * Carta Si (037)   * pinless debit (038)   * encoded account (039)   * UATP (040)   * Household (041)   * Maestro (042) - International   * GE Money UK (043)   * Korean cards (044)   * Style (045)   * JCrew (046)   * PayEase China processing eWallet (047)   * PayEase China processing bank transfer (048)   * Meijer Private Label (049)   * Hipercard (050) — supported only by the Comercio Latino processor.   * Aura (051) — supported only by the Comercio Latino processor.   * Redecard (052)   * ORICO (053)   * Elo (054) — supported only by the Comercio Latino processor.   * Capital One Private Label (055)   * Synchrony Private Label (056)   * Costco Private Label (057)   * mada (060)   * China Union Pay (062)   * Falabella private label (063) 

        :return: The type of this PaymentInstrumentCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PaymentInstrumentCard.
        Type of credit card. Possible values:   * Visa (001)   * Mastercard (002) - Eurocard—European regional brand of Mastercard   * American Express (003)   * Discover (004)   * Diners Club (005)   * Carte Blanche (006)   * JCB (007)   * Optima (008)   * Twinpay Credit (011)   * Twinpay Debit (012)   * Walmart (013)   * EnRoute (014)   * Lowes consumer (015)   * Home Depot consumer (016)   * MBNA (017)   * Dicks Sportswear (018)   * Casual Corner (019)   * Sears (020)   * JAL (021)   * Disney (023)   * Maestro (024) - UK Domestic   * Sams Club consumer (025)   * Sams Club business (026)   * Nicos (027)   * Bill me later (028)   * Bebe (029)   * Restoration Hardware (030)   * Delta (031) — use this value only for Ingenico ePayments. For other processors, use 001 for all Visa card types.   * Solo (032)   * Visa Electron (033)   * Dankort (034)   * Laser (035)   * Carte Bleue (036) — formerly Cartes Bancaires   * Cartes Bancaires (036)   * Carta Si (037)   * pinless debit (038)   * encoded account (039)   * UATP (040)   * Household (041)   * Maestro (042) - International   * GE Money UK (043)   * Korean cards (044)   * Style (045)   * JCrew (046)   * PayEase China processing eWallet (047)   * PayEase China processing bank transfer (048)   * Meijer Private Label (049)   * Hipercard (050) — supported only by the Comercio Latino processor.   * Aura (051) — supported only by the Comercio Latino processor.   * Redecard (052)   * ORICO (053)   * Elo (054) — supported only by the Comercio Latino processor.   * Capital One Private Label (055)   * Synchrony Private Label (056)   * Costco Private Label (057)   * mada (060)   * China Union Pay (062)   * Falabella private label (063) 

        :param type: The type of this PaymentInstrumentCard.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["visa", "mastercard", "american express", "discover", "diners club", "carte blanche", "jcb", "optima", "twinpay credit", "twinpay debit", "walmart", "enroute", "lowes consumer", "home depot consumer", "mbna", "dicks sportswear", "casual corner", "sears", "jal", "disney", "maestro uk domestic", "sams club consumer", "sams club business", "nicos", "bill me later", "bebe", "restoration hardware", "delta online", "solo", "visa electron", "dankort", "laser", "carte bleue", "carta si", "pinless debit", "encoded account", "uatp", "household", "maestro international", "ge money uk", "korean cards", "style", "jcrew", "payease china processing ewallet", "payease china processing bank transfer", "meijer private label", "hipercard", "aura", "redecard", "orico", "elo", "capital one private label", "synchrony private label", "china union pay", "costco private label", "mada", "falabella private label"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def issue_number(self):
        """
        Gets the issue_number of this PaymentInstrumentCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder.

        :return: The issue_number of this PaymentInstrumentCard.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """
        Sets the issue_number of this PaymentInstrumentCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder.

        :param issue_number: The issue_number of this PaymentInstrumentCard.
        :type: str
        """
        if issue_number is not None and len(issue_number) > 2:
            raise ValueError("Invalid value for `issue_number`, length must be less than or equal to `2`")
        if issue_number is not None and len(issue_number) < 1:
            raise ValueError("Invalid value for `issue_number`, length must be greater than or equal to `1`")

        self._issue_number = issue_number

    @property
    def start_month(self):
        """
        Gets the start_month of this PaymentInstrumentCard.
        Month of the start of the Maestro (UK Domestic) card validity period.  Format: `MM`. Possible values: `01` through `12`. 

        :return: The start_month of this PaymentInstrumentCard.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """
        Sets the start_month of this PaymentInstrumentCard.
        Month of the start of the Maestro (UK Domestic) card validity period.  Format: `MM`. Possible values: `01` through `12`. 

        :param start_month: The start_month of this PaymentInstrumentCard.
        :type: str
        """
        if start_month is not None and len(start_month) > 2:
            raise ValueError("Invalid value for `start_month`, length must be less than or equal to `2`")
        if start_month is not None and len(start_month) < 2:
            raise ValueError("Invalid value for `start_month`, length must be greater than or equal to `2`")

        self._start_month = start_month

    @property
    def start_year(self):
        """
        Gets the start_year of this PaymentInstrumentCard.
        Year of the start of the Maestro (UK Domestic) card validity period.  Format: `YYYY`. Possible values: `1900` through `2099`. 

        :return: The start_year of this PaymentInstrumentCard.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this PaymentInstrumentCard.
        Year of the start of the Maestro (UK Domestic) card validity period.  Format: `YYYY`. Possible values: `1900` through `2099`. 

        :param start_year: The start_year of this PaymentInstrumentCard.
        :type: str
        """
        if start_year is not None and len(start_year) > 4:
            raise ValueError("Invalid value for `start_year`, length must be less than or equal to `4`")
        if start_year is not None and len(start_year) < 4:
            raise ValueError("Invalid value for `start_year`, length must be greater than or equal to `4`")

        self._start_year = start_year

    @property
    def use_as(self):
        """
        Gets the use_as of this PaymentInstrumentCard.
        Card Use As Field. Supported value of `pinless debit` only. Only for use with Pinless Debit tokens.

        :return: The use_as of this PaymentInstrumentCard.
        :rtype: str
        """
        return self._use_as

    @use_as.setter
    def use_as(self, use_as):
        """
        Sets the use_as of this PaymentInstrumentCard.
        Card Use As Field. Supported value of `pinless debit` only. Only for use with Pinless Debit tokens.

        :param use_as: The use_as of this PaymentInstrumentCard.
        :type: str
        """

        self._use_as = use_as

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
        if not isinstance(other, PaymentInstrumentCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
