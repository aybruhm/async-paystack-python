# Stdlib Imports
import json
from typing import Dict, Tuple, Union

# Own Imports
from async_paystack.services.base_paystack import PayStack

# Third Party Imports
import httpx


class Transfers(PayStack):
    """
    The Transfer API Wrapper allows you to send money to bank accounts
    and mobile money wallet.
    """

    async def create_transfer_recipient(
        self, nuban: str, name: str, account_number: str, bank_code: str, currency: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function creates a transfer recipient

        :param nuban: The NUBAN (Nigerian Uniform Bank Account Number) of the recipient
        :type nuban: str
        :param name: The name of the recipient
        :type name: str
        :param account_number: The account number of the recipient
        :type account_number: str
        :param bank_code: The bank code of the bank you want to transfer to
        :type bank_code: str
        :param currency: The currency of the account. This should be NGN for Nigerian Naira
        :type currency: str
        :return: A tuple of the status and the data.

        See More: https://paystack.com/docs/api/#transfer-recipient-create
        """  # noqa: E501

        async with httpx.AsyncClient() as client:
            data = {
                "type": f"{nuban}",
                "name": f"{name}",
                "account_number": f"{account_number}",
                "bank_code": f"{bank_code}",
                "currency": f"{currency}",
            }
            url = self.base_url = "transferrecipient"

            response = await client.post(
                url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]

    async def initiate_transfer(
        self, source: str, amount: int, recipient_code: str, reason: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function initiates a transfer from your account to another account

        :param source: The source (balance) wallet or account to debit the funds from
        :type source: str
        :param amount: The amount to be transferred
        :type amount: int
        :param recipient_code: The recipient's code you got from the `create_transfer_recipient` function
        :type recipient_code: str
        :param reason: The reason for the transfer
        :type reason: str
        :return: A tuple of the status and the data.

        See More: https://paystack.com/docs/api/#transfer-initiate
        """  # noqa: E501

        async with httpx.AsyncClient() as client:
            data = {
                "source": f"{source}",
                "amount": int(amount),
                "recipient": f"{recipient_code}",
                "reason": f"{reason}",
            }
            url = self.base_url + "transfer"

            response = await client.post(
                url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]

    async def complete_transfer(
        self, transfer_code: str, otp_code: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function completes a transfer initiated by the `initiate_transfer` function

        :param transfer_code: The transfer code you got from the `initiate_transfer` method
        :type transfer_code: str
        :param otp_code: The OTP code sent to the recipient's phone number
        :type otp_code: str
        :return: A tuple of the status and the data.

        See More: https://paystack.com/docs/api/#transfer-finalize
        """  # noqa: E501

        async with httpx.AsyncClient() as client:
            data = {"transfer_code": f"{transfer_code}", "otp": f"{otp_code}"}
            url = self.base_url + "transfer/finalize_transfer"

            response = await client.post(
                url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]
