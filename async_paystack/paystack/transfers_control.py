# Own Imports
from async_paystack.services import PayStack

# Typing Imports
from typing import Dict, Tuple

# Third Party Imports
import httpx

# Native Imports
import json


class TransfersControl(PayStack):
    """
    The Transfers Control API Wrapper allows you manage settings of your transfers.
    """
    
    async def check_balance(self) -> Tuple[Dict, Dict]:
        """
        This function fetch the available balance on your account
        
        :return: A tuple of two dictionaries.
        
        See More: https://paystack.com/docs/api/#transfer-control-balance
        """
        
        async with httpx.AsyncClient() as client:
            url = self.BASE_URL + "balance"
            response = await client.get(url=url, headers=json.dumps(self.headers))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["messagge"]
            
    
    async def fetch_ledger_balance(self) -> Tuple[Dict, Dict]:
        """
        This function fetch all pay-ins and pay-outs that occured on your integration
        
        :return: A tuple of two dictionaries.
        
        See More: https://paystack.com/docs/api/#transfer-control-balance-ledger
        """
        
        async with httpx.AsyncClient() as client:
            url = self.BASE_URL + "balance/ledger"
            response = await client.get(url=url, headers=json.dumps(self.headers))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
            
        
    async def resend_transfers_otp(self, transfer_code:str, reason:str) -> Tuple[Dict, Dict]:
        """
        This function resends the OTP for a transfer
        
        :param transfer_code: The transfer code of the transfer you want to resend the OTP for
        :type transfer_code: str
        :param reason: The reason for resending the OTP
        :type reason: str
        :return: A tuple of two dictionaries.
        
        See More: https://paystack.com/docs/api/#transfer-control-resend-otp
        """
        
        async with httpx.AsyncClient() as client:
            
            data = {
                "transfer_code": f"{transfer_code}",
                "reason": f"{reason}"
            }
            url = self.BASE_URL + "transfer/resend_otp"
            response = await client.post(url=url, headers=json.dumps(self.headers), data=json.dumps(data))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
            
    
    async def disable_transfers_otp(self) -> Tuple[Dict, Dict]:
        """
        This function disables the OTP for transfers
        :return: A tuple of two dictionaries.
        
        See More: https://paystack.com/docs/api/#transfer-control-disable-otp
        """
        
        async with httpx.AsyncClient() as client:
            url = self.BASE_URL + "transfer/disable_otp"
            response = await client.post(url=url, headers=json.dumps(self.headers))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
            
            
    async def finalize_disable_otp(self, otp:str) ->  Tuple[Dict, Dict]:
        """
        This function is used to finalize the disabling of OTP for transfers
        
        :param otp: The OTP you received from the previous step
        :type otp: str
        :return: A tuple of two dictionaries.
        
        Read More: https://paystack.com/docs/api/#transfer-control-finalize-disable-otp
        """
        
        async with httpx.AsyncClient() as client:
            
            data = {
                "otp": f"{otp}"
            }
            url = self.BASE_URL + "transfer/disable_otp_finalize"
            response = await client.post(url=url, headers=json.dumps(self.headers), data=json.dumps(data))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]
            
    
    async def enable_transfers_otp(self, otp:str) -> Tuple[Dict, Dict]:
        """
        This function enables the transfer of funds from your account to another account
        
        :param otp: The OTP you received from the enable_transfers method
        :type otp: str
        :return: A tuple of two dictionaries.
        
        See More: https://paystack.com/docs/api/#transfer-control-enable-otp
        """
        
        async with httpx.AsyncClient() as client:
            
            url = self.BASE_URL + "transfer/enable_otp"
            response = await client.post(url=url, headers=json.dumps(self.headers))
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["status"], response_data["data"]
            
            else:
                response_data = response.json()
                return response_data["status"], response_data["message"]