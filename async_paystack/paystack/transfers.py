# Own Imports
from async_paystack.services import PayStack

# Typing Imports
from typing import Dict, Tuple

# Third Party Imports
import httpx

# Native Imports
import json


class Transfers(PayStack):
    """
    The Transfer API Wrapper allows you to send money to bank accounts and mobile money wallet.
    """
            
    async def validate_account_number(
        self, bank_code:str, country_code:str, account_number:str, 
        account_name:str, account_type:str, document_type:str, document_number:str) -> Tuple[Dict, Dict]:
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
                "document_number": f"{document_number}"
            }
            url = self.BASE_URL + "bank/validate"
            response = await client.post(url, headers=json.dumps(self.headers), data=json.dumps(data))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
    
    
    async def create_transfer_recipient(self, nuban:str, name:str, account_number:str, bank_code:str, currency:str) -> Tuple[Dict, Dict]:
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
        :return: A tuple of two dictionaries.

        See More: https://paystack.com/docs/api/#transfer-recipient-create
        """
        
        async with httpx.AsyncClient() as client:
            
            data = {
                "type": f"{nuban}",
                "name": f"{name}",
                "account_number": f"{account_number}",
                "bank_code": f"{bank_code}",
                "currency": f"{currency}",
            }
            url = self.BASE_URL = "transferrecipient"
            response = await client.post(url, headers=json.dumps(self.headers), data=json.dumps(data))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
    
    
    async def initiate_transfer(self, source:str, amount:int, recipient_code:str, reason:str) -> Tuple[Dict, Dict]:
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
        :return: A tuple of two dictionaries.

        See More: https://paystack.com/docs/api/#transfer-initiate
        """
        
        async with httpx.AsyncClient() as client:
            
            data = {
                "source": f"{source}",
                "amount": int(amount), 
                "recipient": f"{recipient_code}",
                "reason": f"{reason}", 
            }
            url = self.BASE_URL + "transfer"
            response = await client.post(url, headers=json.dumps(self.headers), data=json.dumps(data))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
        
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
            
    
    async def complete_transfer(self, transfer_code:str, otp_code:str) -> Tuple[Dict, Dict]:
        """
        This function completes a transfer initiated by the `initiate_transfer` function
        
        :param transfer_code: The transfer code you got from the `initiate_transfer` method
        :type transfer_code: str
        :param otp_code: The OTP code sent to the recipient's phone number
        :type otp_code: str
        :return: A tuple of two dictionaries.

        See More: https://paystack.com/docs/api/#transfer-finalize
        """
        
        async with httpx.AsyncClient() as client:
            
            data = { 
                "transfer_code": f"{transfer_code}", 
                "otp": f"{otp_code}"
            }
            url = self.BASE_URL + "transfer/finalize_transfer"
            response = await client.post(url, headers=json.dumps(self.headers), data=json.dumps(data))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]