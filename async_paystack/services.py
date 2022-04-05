import requests
import json


class PayStack:
    PAYSTACK_SECRET_KEY = ""
    BASE_URL = "https://api.paystack.co/"
    

    @classmethod
    def verify_payment(self, ref:str):
        """
        Verify a payment made to your account
        
        :param ref: The reference you want to verify
        :return: The response data is a dictionary with two keys, status and data.
        The status key returns a boolean value indicating whether the request was successful or not.
        The data key returns a dictionary with the transaction details.
        """
        
        path = f"transaction/verify/{ref}"

        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        url = self.BASE_URL + path
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]

        response_data = response.json()
        return response_data["status"], response_data["message"]


    @classmethod
    def resolve_account_number(self, account_number:int, account_code:int):
        """
        It resolves the account number of a bank account
        
        :param account_number: The account number of the customer to resolve
        :param account_code: This is the bank account number
        :return: The resolve_account_number function returns a tuple of two values. The first value is a
        boolean value which is True if the account number is valid and False if it is not. The second value
        is a dictionary of the account details.
        """
        
        path = f"bank/resolve?account_number={account_number}&bank_code={account_code}"

        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        url = self.BASE_URL + path
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]

        response_data = response.json()
        return response_data["status"], response_data["message"]


    @classmethod
    def resolves_bank_verif_number(self, first_name:str, last_name:str, bvn:int, account_number:int):
        """
        It takes in a first name, last name, bvn and account number and returns a status and data
        
        :param first_name: The first name of the customer
        :param last_name: The last name of the customer
        :param bvn: The BVN of the user whose account you want to verify
        :param account_number: The account number of the customer
        :return: The status of the request and the data.
        """

        path = "/bvn/match"

        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "bvn": f"{bvn}",
            "account_number": f"{account_number}",
            "bank_code": "058",
            "first_name": f"{first_name}",
            "last_name": f"{last_name}",
        }
        data_json = json.dumps(data, indent=4)

        url = self.BASE_URL + path
        response = requests.post(url, headers=headers, data=data_json)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]

        response_data = response.json()
        return response_data["status"], response_data["message"]

