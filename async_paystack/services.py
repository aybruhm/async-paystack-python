# Native Imports
import sys, os

# Own Imports
from async_paystack import config

# Third party Imports
from decouple import config as env_config



# Adding the parent directory to the path 
# so that the `config.py` file can be imported.
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(dir))



class PayStack:
    """
    Base Paystack Async API Wrapper
    
    `SECRET_KEY:` do not expose this in production
    `BASE_URL: ` base url of paystack api
    """
    # global config
    # Secret_Key: Do not expose this in production
    PAYSTACK_SECRET_KEY = config.paystack_secret_key(PAYSTACK_SECRET_KEY = env_config("PAYSTACK_SECRET_KEY"))
    BASE_URL = "https://api.paystack.co/"
    
    # authentication headers for paystack
    headers = config.authorization_headers(secret_key=PAYSTACK_SECRET_KEY)
    