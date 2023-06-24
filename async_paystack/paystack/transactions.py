# Stdlib Imports
import json
from typing import Dict, Tuple, Union

# Own Imports
from async_paystack.services.base_paystack import PayStack

# Third Party Imports
import httpx


class Transactions(PayStack):
    """
    The Transactions API Wrapper allows you create and manage
    payments on your integration.
    """

    async def initiate_transaction(
        self, user_email: str, amount: int
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function initiates a transaction for a user

        :param user_email: The email of the user you want to initiate a transaction for
        :type user_email: str
        :param amount: The amount to be charged
        :type amount: int

        :return::return:  A tuple of the status and the data.
        """

        async with httpx.AsyncClient() as client:
            data = {"email": f"{user_email}", "amount": int(amount)}
            url = self.base_url + "transaction/initialize"
            
            response = await client.post(
                url, headers=self.headers(), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["messsage"]

    async def verify_transaction(self, ref: str) -> Tuple[bool, Union[Dict, str]]:
        """
        This function verifies a transaction using the transaction reference

        :param ref: The transaction reference number
        :type ref: str
        :return::return:  A tuple of the status and the data.
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + f"transaction/verify/{ref}"
            response = await client.get(url, headers=self.headers())

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["messsage"]

    async def list_transactions(self) -> Tuple[bool, Union[Dict, str]]:
        """
        This function gets list of transactions carried out on your integration.

        :return::return:  A tuple of the status and the data.
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + "transaction"
            response = await client.get(url, headers=self.headers())

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["messsage"]

    async def fetch_transaction(self, id: int) -> Tuple[bool, Union[Dict, str]]:
        """
        This function get details of a transaction carried out on your integration.

        :return A tuple of two dictionaries.
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + f"transaction/{id}"
            response = await client.get(url, headers=self.headers())

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["messsage"]

    async def charge_authorization(
        self, authorization_code: str, email: str, amount: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function charges an authorization code for subsequently (reoccuring) payments.

        :param authorization_code: The authorization code returned from the authorized call.
        :type authorization_code: str
        :param email: The email address of the customer
        :type email: str
        :param amount: The amount to be charged
        :type amount: str
        :return::return:  A tuple of the status and the data.
        """  # noqa: E501

        async with httpx.AsyncClient() as client:
            data = {
                "authorization_code": f"{authorization_code}",
                "email": f"{email}",
                "amount": int(amount),
            }
            url = self.base_url + "transaction/charge_authorization"
            response = await client.post(
                url, headers=self.headers(), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["messsage"]

    async def check_authorization(
        self, email: str, amount: str, authorization_code: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function checks the authorization code of a transaction

        `(You shouldn't use this function to check a card for sufficient funds
        if you are going to charge the user immediately.
        This is because we hold funds when this endpoint is called which can
        lead to an insufficient funds error.)`

        Read more https://paystack.com/docs/api/#transaction-check-authorization

        :param email: The email address of the customer
        :type email: str
        :param amount: The amount to be charged
        :type amount: str
        :param authorization_code: This is the authorization code you get from \
            the user after they have authorized the transaction
        :type authorization_code: str
        :return::return:  A tuple of the status and the data.
        """

        async with httpx.AsyncClient() as client:
            data = {
                "email": f"{email}",
                "amount": f"{amount}",
                "authorization_code": f"{authorization_code}",
            }
            url = self.base_url + "transaction/check_authorization"
            response = await client.post(
                url, headers=self.headers(), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["messsage"]
