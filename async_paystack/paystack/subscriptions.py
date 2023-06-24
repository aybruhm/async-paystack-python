# Stdlib Imports
import json
from typing import Dict, Tuple, Union

# Own Imports
from async_paystack.services import PayStack

# Third Party Imports
import httpx


class Subscriptions(PayStack):
    """
    The Subscriptions API Wrapper allows you create and manage
    recurring payment on your integration
    """

    async def create_subscription(
        self, customer: str, plan: str, authorization: str = None
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function creates a subscription for a customer on a plan

        :param customer: The customer's ID on your platform
        :type customer: str
        :param plan: The plan ID of the plan you want to subscribe the customer to
        :type plan: str
        :param authorization: The authorization code you received from \
            the customer's bank
        :type authorization: str
        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#subscription-create
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + "subscription"
            data = {
                "customer": f"{customer}",
                "plan": f"{plan}",
            }

            if authorization:
                data["authorization"] = f"{authorization}"

            response = await client.post(
                url=url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            else:
                response_data = response.json()
                return response_data["status"], response_data["messsage"]

    async def list_subscriptions(self) -> Tuple[bool, Union[Dict, str]]:
        """
        This function fetch subscriptions available on your integration.

        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#subscription-create
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + "subscription"
            response = await client.get(url=url, headers=json.dumps(self.headers()))

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]

    async def fetch_subscription(
        self, id_or_code: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        It fetches a subscription by its id or code

        :param id_or_code: The subscription ID or code
        :type id_or_code: str
        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#subscription-fetch
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + f"subscription/{id_or_code}"
            response = await client.get(url=url, headers=json.dumps(self.headers()))

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]

    async def enable_subscription(
        self, code: str, token: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function enables a subscription

        :param code: The code you received from the user
        :type code: str
        :param token: The token you received from the user
        :type token: str
        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#subscription-enable
        """

        async with httpx.AsyncClient() as client:
            data = {"code": f"{code}", "token": f"{token}"}
            url = self.base_url + "subscription/enable"

            response = await client.post(
                url=url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]

    async def disable_subscription(
        self, code: str, token: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function disables a subscription plan for a user

        :param code: The code of the subscription plan you want to disable
        :type code: str
        :param token: The token of the user you want to disable subscription for
        :type token: str
        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#subscription-disable
        """

        async with httpx.AsyncClient() as client:
            data = {"code": f"{code}", "token": f"{token}"}
            url = self.base_url + "subscription/disable"

            response = await client.post(
                url=url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]

    async def generate_update_subscription_link(
        self, code: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        It generates a link that can be used to update a subscription

        :param code: The code of the subscription you want to generate a link for
        :type code: str
        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#subscription-disable
        """

        async with httpx.AsyncClient() as client:
            data = {"code": f"{code}"}
            url = self.base_url + f"subscription/{code}/manage/link/"

            response = await client.post(
                url=url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]

    async def send_update_subscription_link(
        self, code: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function sends a link to the user's email address to \
            update their subscription

        :param code: The code of the subscription you want to update
        :type code: str
        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#subscription-manage-email
        """

        async with httpx.AsyncClient() as client:
            data = {"code": f"{code}"}
            url = self.base_url + f"subscription/{code}/manage/email/"

            response = await client.post(
                url=url, headers=json.dumps(self.headers()), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
