from os import environ
from typing import Dict


# Paystack Secret Key
PAYSTACK_SECRET_KEY = environ.get('PAYSTACK_SECRET_KEY')

# Authorization Headers Definition
def authorization_headers(secret_key:str) -> Dict[str,str]:
    """
    It takes a secret key and returns a dictionary of headers that can be 
    used to make requests to the API
    
    :param secret_key: The secret key you got from the API page
    :type secret_key: str
    :return: A dictionary with the key "Authorization" and the value "Bearer {secret_key}"
    """
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }
    return headers