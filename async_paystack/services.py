# Stdlib Imports
import os
import sys

# Third party Imports
from decouple import config as env



# Adding the parent directory to the path 
# so that the `config.py` file can be imported.
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(dir))


class PayStack:
    """
    Base Paystack Async API Wrapper
    """
    
    def __init__(self) -> None:
        self.base_url = env("PAYSTACK_BASE_URL")
        self.secret_key = env("PAYSTACK_SECRET_KEY")
    
    def headers(self) -> dict:
        return {
        "Authorization": f"Bearer {self.secret_key}",
        "Content-Type": "application/json"
    }