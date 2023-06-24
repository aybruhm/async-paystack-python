# Stdlib Imports
import json
import secrets
from unittest import mock

# Own Imports
from async_paystack.paystack.transactions import Transactions

# Third Party Imports
import pytest


@pytest.mark.asyncio
async def test_initiate_transaction():
    # Initialize transactions class
    trx = Transactions()

    # Set transaction reference
    trx_reference = secrets.token_hex(8)

    # Mock the httpx.AsyncClient and its post method
    mock_client = mock.AsyncMock()
    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_client.post.return_value = mock_response
    
    #? note: the data isn't complete.
    #? i am only using reference, because it is the easiest to duplicae :-)
    mock_response.json.return_value = {
        "status": True,
        "data": {"reference": f"{trx_reference}"},
    }

    # Set the mocked client as the client used in the function
    trx.client = mock_client

    # Call the function with test data
    user_email = "test@example.com"
    amount = 100 * 100
    status, data = await trx.initiate_transaction(user_email, amount, trx_reference)

    # Assert the expected behavior
    assert (status, data["reference"]) == (True, f"{trx_reference}")
