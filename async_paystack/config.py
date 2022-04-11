from typing import Dict, String


# Paystack Secret Key
def paystack_secret_key(PAYSTACK_SECRET_KEY:str) -> String:
    """
    It gets the secret key from the environment variable and returns it
    
    :param secret_key: This is the secret key you got from your Paystack dashboard
    :type secret_key: str
    :return: The secret key is being returned.
    """
    secret_key = PAYSTACK_SECRET_KEY
    return secret_key


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