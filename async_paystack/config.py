from os import environ
from typing import Dict


# Paystack Secret Key
PAYSTACK_SECRET_KEY = environ.get('PAYSTACK_SECRET_KEY')

# Authorization Headers
def authorization_headers(secret_key:str) -> Dict[str,str]:
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }
    return headers