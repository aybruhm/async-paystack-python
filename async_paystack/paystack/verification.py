# Stdlib Imports
import json
from typing import Dict, Tuple, Union

# Own Imports
from async_paystack.services.base_paystack import PayStack

# Third Party Imports
import httpx


class Verification(PayStack):
    """The Verification API Wrapper allows you perform KYC processes"""

    async def resolves_account_number(
        self, account_number: str, bank_code: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function verifies the account number

        :param account_number: The account number of the bank account you want to verify
        :type account_number: str
        :param bank_code: The bank code of the bank you want to verify the account number for
        :type bank_code: str
        :return: A tuple of two dictionaries.

        Read More: https://paystack.com/docs/api#verification-resolve-account
        """ # noqa: E501

        async with httpx.AsyncClient() as client:
            url = (
                self.base_url
                + f"bank/resolve?account_number={account_number}&bank_code={bank_code}"
            )
            response = await client.get(url, headers=json.dumps(self.headers()))

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]

    async def validate_account_number(
        self,
        bank_code: str,
        country_code: str,
        account_number: str,
        account_name: str,
        account_type: str,
        document_type: str,
        document_number: str,
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function validates a customer's bank account number

        :param bank_code: The bank code of the customer's bank
        :type bank_code: str
        :param country_code: The two digit ISO code of the customer's bank
        :type country_code: str
        :param account_number: Customer's account number
        :type account_number: str
        :param account_name: Customer's first and last name registered with their bank
        :type account_name: str
        :param account_type: This can take one of: [ personal, business ]
        :type account_type: str
        :param document_type: This can take one of: [ identityNumber, passportNumber,
        businessRegistrationNumber ]
        :type document_type: str
        :param document_number: This is the customer's identity number
        :type document_number: str
        :return: A tuple of two dictionaries.

        See More: https://paystack.com/docs/api/#verification-validate-account
        """

        async with httpx.AsyncClient() as client:
            data = {
                "bank_code": f"{bank_code}",
                "country_code": f"{country_code}",
                "account_number": f"{account_number}",
                "account_name": f"{account_name}",
                "account_type": f"{account_type}",
                "document_type": f"{document_type}",
                "document_number": f"{document_number}",
            }
            url = self.base_url + "bank/validate"
            response = await client.post(
                url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]

    async def resolve_card_bin(self, bin: str) -> Tuple[bool, Union[Dict, str]]:
        """
        This function verifies a card bin and get more information about the customer's


        :param bin: The first 6 digits of the card number
        :type bin: str
        :return: A tuple of two dictionaries.

        Read More: https://paystack.com/docs/api/#verification-resolve-card
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + f"decision/bin/{bin}"
            response = await client.get(url=url, headers=json.dumps(self.headers()))

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]
