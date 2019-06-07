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


class PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures(object):
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
        'account_type': 'str',
        'account_status': 'str',
        'balance_amount': 'str',
        'balance_amount_type': 'str',
        'currency': 'str',
        'balance_sign': 'str',
        'affluence_indicator': 'str',
        'category': 'str',
        'commercial': 'str',
        'group': 'str',
        'health_care': 'str',
        'payroll': 'str',
        'level3_eligible': 'str',
        'pinless_debit': 'str',
        'signature_debit': 'str',
        'prepaid': 'str',
        'regulated': 'str'
    }

    attribute_map = {
        'account_type': 'accountType',
        'account_status': 'accountStatus',
        'balance_amount': 'balanceAmount',
        'balance_amount_type': 'balanceAmountType',
        'currency': 'currency',
        'balance_sign': 'balanceSign',
        'affluence_indicator': 'affluenceIndicator',
        'category': 'category',
        'commercial': 'commercial',
        'group': 'group',
        'health_care': 'healthCare',
        'payroll': 'payroll',
        'level3_eligible': 'level3Eligible',
        'pinless_debit': 'pinlessDebit',
        'signature_debit': 'signatureDebit',
        'prepaid': 'prepaid',
        'regulated': 'regulated'
    }

    def __init__(self, account_type=None, account_status=None, balance_amount=None, balance_amount_type=None, currency=None, balance_sign=None, affluence_indicator=None, category=None, commercial=None, group=None, health_care=None, payroll=None, level3_eligible=None, pinless_debit=None, signature_debit=None, prepaid=None, regulated=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures - a model defined in Swagger
        """

        self._account_type = None
        self._account_status = None
        self._balance_amount = None
        self._balance_amount_type = None
        self._currency = None
        self._balance_sign = None
        self._affluence_indicator = None
        self._category = None
        self._commercial = None
        self._group = None
        self._health_care = None
        self._payroll = None
        self._level3_eligible = None
        self._pinless_debit = None
        self._signature_debit = None
        self._prepaid = None
        self._regulated = None

        if account_type is not None:
          self.account_type = account_type
        if account_status is not None:
          self.account_status = account_status
        if balance_amount is not None:
          self.balance_amount = balance_amount
        if balance_amount_type is not None:
          self.balance_amount_type = balance_amount_type
        if currency is not None:
          self.currency = currency
        if balance_sign is not None:
          self.balance_sign = balance_sign
        if affluence_indicator is not None:
          self.affluence_indicator = affluence_indicator
        if category is not None:
          self.category = category
        if commercial is not None:
          self.commercial = commercial
        if group is not None:
          self.group = group
        if health_care is not None:
          self.health_care = health_care
        if payroll is not None:
          self.payroll = payroll
        if level3_eligible is not None:
          self.level3_eligible = level3_eligible
        if pinless_debit is not None:
          self.pinless_debit = pinless_debit
        if signature_debit is not None:
          self.signature_debit = signature_debit
        if prepaid is not None:
          self.prepaid = prepaid
        if regulated is not None:
          self.regulated = regulated

    @property
    def account_type(self):
        """
        Gets the account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Type of account. This value is returned only if you requested a balance inquiry. Possible values:   - `00`: Not applicable or not specified  - `10`: Savings account  - `20`: Checking account  - `30`: Credit card account  - `40`: Universal account 

        :return: The account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Type of account. This value is returned only if you requested a balance inquiry. Possible values:   - `00`: Not applicable or not specified  - `10`: Savings account  - `20`: Checking account  - `30`: Credit card account  - `40`: Universal account 

        :param account_type: The account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if account_type is not None and len(account_type) > 2:
            raise ValueError("Invalid value for `account_type`, length must be less than or equal to `2`")

        self._account_type = account_type

    @property
    def account_status(self):
        """
        Gets the account_status of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Possible values:   - `N`: Nonregulated  - `R`: Regulated  **Note** This field is returned only for CyberSource through VisaNet. 

        :return: The account_status of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """
        Sets the account_status of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Possible values:   - `N`: Nonregulated  - `R`: Regulated  **Note** This field is returned only for CyberSource through VisaNet. 

        :param account_status: The account_status of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if account_status is not None and len(account_status) > 1:
            raise ValueError("Invalid value for `account_status`, length must be less than or equal to `1`")

        self._account_status = account_status

    @property
    def balance_amount(self):
        """
        Gets the balance_amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Remaining balance on the account. 

        :return: The balance_amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._balance_amount

    @balance_amount.setter
    def balance_amount(self, balance_amount):
        """
        Sets the balance_amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Remaining balance on the account. 

        :param balance_amount: The balance_amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if balance_amount is not None and len(balance_amount) > 12:
            raise ValueError("Invalid value for `balance_amount`, length must be less than or equal to `12`")

        self._balance_amount = balance_amount

    @property
    def balance_amount_type(self):
        """
        Gets the balance_amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Type of amount. This value is returned only if you requested a balance inquiry. The issuer determines the value that is returned. Possible values for deposit accounts:   - `01`: Current ledger (posted) balance.  - `02`: Current available balance, which is typically the ledger balance less outstanding authorizations.  Some depository institutions also include pending deposits and the credit or overdraft line associated with the account. Possible values for credit card accounts:   - `01`: Credit amount remaining for customer (open to buy).  - `02`: Credit limit. 

        :return: The balance_amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._balance_amount_type

    @balance_amount_type.setter
    def balance_amount_type(self, balance_amount_type):
        """
        Sets the balance_amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Type of amount. This value is returned only if you requested a balance inquiry. The issuer determines the value that is returned. Possible values for deposit accounts:   - `01`: Current ledger (posted) balance.  - `02`: Current available balance, which is typically the ledger balance less outstanding authorizations.  Some depository institutions also include pending deposits and the credit or overdraft line associated with the account. Possible values for credit card accounts:   - `01`: Credit amount remaining for customer (open to buy).  - `02`: Credit limit. 

        :param balance_amount_type: The balance_amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if balance_amount_type is not None and len(balance_amount_type) > 2:
            raise ValueError("Invalid value for `balance_amount_type`, length must be less than or equal to `2`")

        self._balance_amount_type = balance_amount_type

    @property
    def currency(self):
        """
        Gets the currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Currency of the remaining balance on the account. For the possible values, see the [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  For details, see `auth_account_balance_currency` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Currency of the remaining balance on the account. For the possible values, see the [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  For details, see `auth_account_balance_currency` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param currency: The currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if currency is not None and len(currency) > 5:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `5`")

        self._currency = currency

    @property
    def balance_sign(self):
        """
        Gets the balance_sign of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Sign for the remaining balance on the account. Returned only when the processor returns this value. Possible values:  Possible values:  - **+**  - **-** 

        :return: The balance_sign of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._balance_sign

    @balance_sign.setter
    def balance_sign(self, balance_sign):
        """
        Sets the balance_sign of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Sign for the remaining balance on the account. Returned only when the processor returns this value. Possible values:  Possible values:  - **+**  - **-** 

        :param balance_sign: The balance_sign of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        allowed_values = ["+", "-"]
        if balance_sign not in allowed_values:
            raise ValueError(
                "Invalid value for `balance_sign` ({0}), must be one of {1}"
                .format(balance_sign, allowed_values)
            )

        self._balance_sign = balance_sign

    @property
    def affluence_indicator(self):
        """
        Gets the affluence_indicator of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        **Chase Paymentech Solutions**  Indicates whether a customer has high credit limits. This information enables you to market high cost items to these customers and to understand the kinds of cards that high income customers are using.  This field is supported for Visa, Mastercard, Discover, and Diners Club. Possible values:   - **Y**: Yes  - **N**: No  - **X**: Not applicable / Unknown  **Litle**  Flag that indicates that a Visa cardholder or Mastercard cardholder is in one of the affluent categories. Possible values:   - **AFFLUENT**: High income customer with high spending pattern (>100k USD annual income and >40k USD annual    card usage).  - **MASS AFFLUENT**: High income customer (>100k USD annual income).  **Processor specific maximum length**:   - Chase Paymentech Solutions: 1  - Litle: 13 

        :return: The affluence_indicator of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._affluence_indicator

    @affluence_indicator.setter
    def affluence_indicator(self, affluence_indicator):
        """
        Sets the affluence_indicator of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        **Chase Paymentech Solutions**  Indicates whether a customer has high credit limits. This information enables you to market high cost items to these customers and to understand the kinds of cards that high income customers are using.  This field is supported for Visa, Mastercard, Discover, and Diners Club. Possible values:   - **Y**: Yes  - **N**: No  - **X**: Not applicable / Unknown  **Litle**  Flag that indicates that a Visa cardholder or Mastercard cardholder is in one of the affluent categories. Possible values:   - **AFFLUENT**: High income customer with high spending pattern (>100k USD annual income and >40k USD annual    card usage).  - **MASS AFFLUENT**: High income customer (>100k USD annual income).  **Processor specific maximum length**:   - Chase Paymentech Solutions: 1  - Litle: 13 

        :param affluence_indicator: The affluence_indicator of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if affluence_indicator is not None and len(affluence_indicator) > 13:
            raise ValueError("Invalid value for `affluence_indicator`, length must be less than or equal to `13`")

        self._affluence_indicator = affluence_indicator

    @property
    def category(self):
        """
        Gets the category of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        #### CyberSource through VisaNet Visa or Mastercard product ID that is associated with the primary account number (PAN). For descriptions of the Visa product IDs, see the Product ID table on the [Visa Request & Response Codes web page.](https://developer.visa.com/guides/request_response_codes)  Data Length: String (3)  #### GPN Visa or Mastercard product ID that is associated with the primary account number (PAN). For descriptions of the Visa product IDs, seepag the Product ID table on the Visa Request & Response Codes web page at https://developer.visa.com/guides/request_response_codes. For descriptions of the Mastercard product IDs, see \"Product IDs\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  Data Length: String (3)  #### Worldpay VAP **Important** Before using this field on Worldpay VAP, you must contact CyberSource Customer Support to have your account configured for this feature.  Type of card used in the transaction. The only possible value is: - `PREPAID`: Prepaid Card  Data Length: String (7)  #### RBS WorldPay Atlanta Type of card used in the transaction. Possible values: - `B`: Business Card - `O`: Noncommercial Card - `R`: Corporate Card - `S`: Purchase Card - `Blank`: Purchase card not supported  Data Length: String (1) 

        :return: The category of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        #### CyberSource through VisaNet Visa or Mastercard product ID that is associated with the primary account number (PAN). For descriptions of the Visa product IDs, see the Product ID table on the [Visa Request & Response Codes web page.](https://developer.visa.com/guides/request_response_codes)  Data Length: String (3)  #### GPN Visa or Mastercard product ID that is associated with the primary account number (PAN). For descriptions of the Visa product IDs, seepag the Product ID table on the Visa Request & Response Codes web page at https://developer.visa.com/guides/request_response_codes. For descriptions of the Mastercard product IDs, see \"Product IDs\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  Data Length: String (3)  #### Worldpay VAP **Important** Before using this field on Worldpay VAP, you must contact CyberSource Customer Support to have your account configured for this feature.  Type of card used in the transaction. The only possible value is: - `PREPAID`: Prepaid Card  Data Length: String (7)  #### RBS WorldPay Atlanta Type of card used in the transaction. Possible values: - `B`: Business Card - `O`: Noncommercial Card - `R`: Corporate Card - `S`: Purchase Card - `Blank`: Purchase card not supported  Data Length: String (1) 

        :param category: The category of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if category is not None and len(category) > 7:
            raise ValueError("Invalid value for `category`, length must be less than or equal to `7`")

        self._category = category

    @property
    def commercial(self):
        """
        Gets the commercial of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a commercial card, which enables you to include Level II data in your transaction requests. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - **Y**: Yes  - **N**: No  - **X**: Not applicable / Unknown  For details, see `auth_card_commercial` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The commercial of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._commercial

    @commercial.setter
    def commercial(self, commercial):
        """
        Sets the commercial of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a commercial card, which enables you to include Level II data in your transaction requests. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - **Y**: Yes  - **N**: No  - **X**: Not applicable / Unknown  For details, see `auth_card_commercial` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param commercial: The commercial of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if commercial is not None and len(commercial) > 1:
            raise ValueError("Invalid value for `commercial`, length must be less than or equal to `1`")

        self._commercial = commercial

    @property
    def group(self):
        """
        Gets the group of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Type of commercial card. This field is supported only for CyberSource through VisaNet. Possible values:   - **B**: Business card  - **R**: Corporate card  - **S**: Purchasing card  - **0**: Noncommercial card 

        :return: The group of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Type of commercial card. This field is supported only for CyberSource through VisaNet. Possible values:   - **B**: Business card  - **R**: Corporate card  - **S**: Purchasing card  - **0**: Noncommercial card 

        :param group: The group of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if group is not None and len(group) > 1:
            raise ValueError("Invalid value for `group`, length must be less than or equal to `1`")

        self._group = group

    @property
    def health_care(self):
        """
        Gets the health_care of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a healthcare card. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_healthcare` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The health_care of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._health_care

    @health_care.setter
    def health_care(self, health_care):
        """
        Sets the health_care of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a healthcare card. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_healthcare` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param health_care: The health_care of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if health_care is not None and len(health_care) > 1:
            raise ValueError("Invalid value for `health_care`, length must be less than or equal to `1`")

        self._health_care = health_care

    @property
    def payroll(self):
        """
        Gets the payroll of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a payroll card. This field is supported for Visa, Discover, Diners Club, and JCB on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_payroll` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The payroll of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._payroll

    @payroll.setter
    def payroll(self, payroll):
        """
        Sets the payroll of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a payroll card. This field is supported for Visa, Discover, Diners Club, and JCB on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_payroll` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param payroll: The payroll of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if payroll is not None and len(payroll) > 1:
            raise ValueError("Invalid value for `payroll`, length must be less than or equal to `1`")

        self._payroll = payroll

    @property
    def level3_eligible(self):
        """
        Gets the level3_eligible of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is eligible for Level III interchange fees, which enables you to include Level III data in your transaction requests. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_level_3_eligible` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The level3_eligible of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._level3_eligible

    @level3_eligible.setter
    def level3_eligible(self, level3_eligible):
        """
        Sets the level3_eligible of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is eligible for Level III interchange fees, which enables you to include Level III data in your transaction requests. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_level_3_eligible` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param level3_eligible: The level3_eligible of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if level3_eligible is not None and len(level3_eligible) > 1:
            raise ValueError("Invalid value for `level3_eligible`, length must be less than or equal to `1`")

        self._level3_eligible = level3_eligible

    @property
    def pinless_debit(self):
        """
        Gets the pinless_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a PINless debit card. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_pinless_debit` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The pinless_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._pinless_debit

    @pinless_debit.setter
    def pinless_debit(self, pinless_debit):
        """
        Sets the pinless_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a PINless debit card. This field is supported for Visa and Mastercard on **Chase Paymentech Solutions**. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_pinless_debit` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param pinless_debit: The pinless_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if pinless_debit is not None and len(pinless_debit) > 1:
            raise ValueError("Invalid value for `pinless_debit`, length must be less than or equal to `1`")

        self._pinless_debit = pinless_debit

    @property
    def signature_debit(self):
        """
        Gets the signature_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a signature debit card.  This information enables you to alter the way an order is processed. For example, you might not want to reauthorize a transaction for a signature debit card, or you might want to perform reversals promptly for a signature debit card. This field is supported for Visa, Mastercard, and Maestro (International) on Chase Paymentech Solutions. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_signature_debit` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The signature_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._signature_debit

    @signature_debit.setter
    def signature_debit(self, signature_debit):
        """
        Sets the signature_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a signature debit card.  This information enables you to alter the way an order is processed. For example, you might not want to reauthorize a transaction for a signature debit card, or you might want to perform reversals promptly for a signature debit card. This field is supported for Visa, Mastercard, and Maestro (International) on Chase Paymentech Solutions. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_signature_debit` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param signature_debit: The signature_debit of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if signature_debit is not None and len(signature_debit) > 1:
            raise ValueError("Invalid value for `signature_debit`, length must be less than or equal to `1`")

        self._signature_debit = signature_debit

    @property
    def prepaid(self):
        """
        Gets the prepaid of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a prepaid card. This information enables you to determine when a gift card or prepaid card is presented for use when establishing a new recurring, installment, or deferred billing relationship.  This field is supported for Visa, Mastercard, Discover, Diners Club, and JCB on Chase Paymentech Solutions. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see the `auth_card_prepaid` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The prepaid of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._prepaid

    @prepaid.setter
    def prepaid(self, prepaid):
        """
        Sets the prepaid of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is a prepaid card. This information enables you to determine when a gift card or prepaid card is presented for use when establishing a new recurring, installment, or deferred billing relationship.  This field is supported for Visa, Mastercard, Discover, Diners Club, and JCB on Chase Paymentech Solutions. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see the `auth_card_prepaid` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param prepaid: The prepaid of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if prepaid is not None and len(prepaid) > 1:
            raise ValueError("Invalid value for `prepaid`, length must be less than or equal to `1`")

        self._prepaid = prepaid

    @property
    def regulated(self):
        """
        Gets the regulated of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is regulated according to the Durbin Amendment. If the card is regulated, the card issuer is subject to price caps and interchange rules. This field is supported for Visa, Mastercard, Discover, Diners Club, and JCB on Chase Paymentech Solutions. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_regulated` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The regulated of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :rtype: str
        """
        return self._regulated

    @regulated.setter
    def regulated(self, regulated):
        """
        Sets the regulated of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        Indicates whether the card is regulated according to the Durbin Amendment. If the card is regulated, the card issuer is subject to price caps and interchange rules. This field is supported for Visa, Mastercard, Discover, Diners Club, and JCB on Chase Paymentech Solutions. Possible values:   - `Y`: Yes  - `N`: No  - `X`: Not applicable / Unknown  For details, see `auth_card_regulated` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param regulated: The regulated of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.
        :type: str
        """
        if regulated is not None and len(regulated) > 1:
            raise ValueError("Invalid value for `regulated`, length must be less than or equal to `1`")

        self._regulated = regulated

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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
