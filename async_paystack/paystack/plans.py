# Stdlib Imports
import json
from typing import Dict, Tuple, Union

# Own Imports
from async_paystack.services.base_paystack import PayStack

# Third Party Imports
import httpx


class Plans(PayStack):
    """
    The Plans API Wrapper allows you create and manage
    installment payment options on your integration.
    """

    async def create_plan(
        self, name: str, interval: str, amount: int
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function creates a plan on your integration.
        
        :param name: The name of the plan
        :type name: str
        :param interval: The frequency with which a customer should be charged. 
        :type interval: str
        :param amount: The amount in kobo. This value must be greater \
            than or equal to 50
        :type amount: int
        :return: A tuple of two dictionaries.
        
        Read More: https://paystack.com/docs/api/#plan-create
        """

        async with httpx.AsyncClient() as client:
            data = {"name": f"{name}", "interval": f"{interval}", "amount": int(amount)}
            url = self.base_url + "plan"

            response = await client.post(
                url=url, headers=self.headers(), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]

    async def list_plans(self) -> Tuple[bool, Union[Dict, str]]:
        """
        This function fetches list plans available on your integration

        :return: A tuple of two dictionaries.

        Read More: https://paystack.com/docs/api/#plan-list
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + "plan"
            response = await client.get(url=url, headers=self.headers())

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]

    async def fetch_plan(self, id_or_code: str) -> Tuple[bool, Union[Dict, str]]:
        """
        This function fetches a plan by its id or code

        :param id_or_code: The ID or code of the plan you want to fetch
        :type id_or_code: str
        :return: A tuple of two dictionaries.

        Read More: https://paystack.com/docs/api/#plan-fetch
        """

        async with httpx.AsyncClient() as client:
            url = self.base_url + f"plan/{id_or_code}"
            response = await client.get(url=url, headers=self.headers())

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]

    async def update_plan(
        self, id_or_code: str, name: str
    ) -> Tuple[bool, Union[Dict, str]]:
        """
        This function updates the name of a plan

        :param id_or_code: The ID or code of the plan to be updated
        :type id_or_code: str
        :param name: The name of the plan
        :type name: str
        :return: A tuple of the status and the data.

        Read More: https://paystack.com/docs/api/#plan-update
        """

        async with httpx.AsyncClient() as client:
            data = {"name": f"{name}"}
            url = self.base_url + f"plan/{id_or_code}"
            response = await client.put(
                url, headers=self.headers(), data=json.dumps(data)
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]

            response_data = response.json()
            return response_data["status"], response_data["message"]
