import json
from os import environ
import aiohttp
from rest_api_payload import success_response, error_response
from async_paystack.config import (
    authorization_headers, paystack_secret_key
)


class PayStack:
    
    # Base url
    BASE_URL = "https://api.paystack.co/"
    
    # Secret_Key: Do not expose this in production
    SECRET_KEY = paystack_secret_key(
        PAYSTACK_SECRET_KEY = environ.get('PAYSTACK_SECRET_KEY')
    )
    
    # Creates an aiohttp client session object.
    session = aiohttp.ClientSession()
    

    @classmethod
    async def verify_payment(self, ref:str):
        """
        Verify a payment made to your account
        
        :param ref: The reference you want to verify
        :return: The response data is a dictionary with two keys, status and data.
        The status key returns a boolean value indicating whether the request was successful or not.
        The data key returns a dictionary with the transaction details.
        """
        
        # Request headers 
        headers = authorization_headers(secret_key=self.SECRET_KEY)
        
        # API endpoint
        path = f"transaction/verify/{ref}"
        
        # API base url + path
        url = self.BASE_URL + path
        
        async with self.session:
            
            response = await self.session.get(url, headers=headers)
            print("Response: ", response)
        
        # # Response from API url
        # response = await self.session.get(url, headers=headers)

        # """This is returning a success response if the request is successful."""
        # if response.status_code == 200:
        #     response_data = response.json()
            
        #     payload = success_response(
        #         status=response_data["status"],
        #         message="Transaction was successfully verified!",
        #         data=response_data["data"]
        #     )
        #     return payload

        # else:
        #     response_data = response.json()
            
        #     payload = error_response(
        #         status=response_data["status"],
        #         message="Transaction failed",
        #         data=response_data["data"] 
        #     )
        #     return payload


    @classmethod
    async def resolves_account_number(self, account_number:int, account_code:int):
        """
        It resolves the account number of a bank account
        
        :param account_number: The account number of the customer to resolve
        :param account_code: This is the bank account number
        :return: The resolve_account_number function returns a tuple of two values. The first value is a
        boolean value which is True if the account number is valid and False if it is not. The second value
        is a dictionary of the account details.
        """
        
        path = f"bank/resolve?account_number={account_number}&bank_code={account_code}"

        headers = authorization_headers()
        
        url = self.BASE_URL + path
        response = self.session.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]

        response_data = response.json()
        return response_data["status"], response_data["message"]


    @classmethod
    async def resolves_bank_verif_number(self, first_name:str, last_name:str, bvn:int, account_number:int):
        """
        It takes in a first name, last name, bvn and account number and returns a status and data
        
        :param first_name: The first name of the customer
        :param last_name: The last name of the customer
        :param bvn: The BVN of the user whose account you want to verify
        :param account_number: The account number of the customer
        :return: The status of the request and the data.
        """

        path = "/bvn/match"

        headers = authorization_headers()
        
        data = {
            "bvn": f"{bvn}",
            "account_number": f"{account_number}",
            "bank_code": "058",
            "first_name": f"{first_name}",
            "last_name": f"{last_name}",
        }
        data_json = json.dumps(data, indent=4)

        url = self.BASE_URL + path
        response = self.session.post(url, headers=headers, data=data_json)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]

        response_data = response.json()
        return response_data["status"], response_data["message"]

