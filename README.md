# Async Paystack Python

Unofficial asynchronous python wrapper for paystack payment.

## Features

## Quickstart

## Example

## Code

```python
async def initiate_transaction(
    self, user_email: str, amount: int, reference: str = None
) -> Tuple[bool, Union[Dict, str]]:
    """
    This function initiates a transaction for a user

    :param user_email: The email of the user you want to initiate a transaction for
    :type user_email: str
    :param amount: The amount to be charged
    :type amount: int
    :param amount: The reference of the transaction
    :type reference: str

    :return::return:  A tuple of the status and the data.
    """

    async with httpx.AsyncClient() as client:
        data = {"email": f"{user_email}", "amount": int(amount)}
        url = self.base_url + "transaction/initialize"
        
        if reference:
            data["reference"] = reference
        
        response = await client.post(
            url, headers=self.headers(), data=json.dumps(data)
        )

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]

        response_data = response.json()
        return response_data["status"], response_data["messsage"]
```

### In action

- To see the code in action, run the following to command to start your python shell: `python` or `python -i` if you are in the same directory of the codebase.
- Write the following codes inside the shell:

    ```shell
    >>> import asyncio
    >>> from async_paystack.paystack.transactions import Transactions
    >>>
    >>>
    >>> trx = Transactions()
    >>> status, data = asyncio.run(trx.initiate_transaction("youremailaddress.com", 50000 * 100, "refrenceisdmik")) # we need to convert naira to kobo before sending to paystack
    >>>
    >>>
    >>> status
    True
    >>> data
    {'authorization_url': 'https://checkout.paystack.com/access_code', 'access_code': 'gibberish', 'reference': 'refrenceisdmik'}
    ```

It is important that when run this code in Django without the asynchronous support, be sure to call the it with the `asyncio.run(...)` method.

### Mock Testing (Explanation)

In the `test_initiate_transaction` example, I:

- Imported the necessary modules and defined the test function using the `@pytest.mark.asyncio` decorator to indicate it's an asynchronous test case.
- Created an instance of the class `(Transactions)` that contains the `initiate_transaction` method to be tested.
- Mocked the `httpx.AsyncClient` class and its post method using `mock.AsyncMock()` and `mock.MagicMock()`, respectively. I set the status_code of the response to `200` and define the JSON response to match the expected behavior.
- Set the mocked client as the client used in the `Transactions` instance by assigning it to the client attribute of the instance.
- Call the `initiate_transaction` method with test data (user_email and amount).
- Asserted that the returned result matches the expected result.
- Finally, I asserted that the post method of the mocked client was called with the expected parameters.

Ensure that the necessary modules (`pytest`, `pytest-asyncio`, `mock`) are installed in your environment for running the test.

## Contribute

All contributions are welcome:

- Read the issues, Fork the project and do a Pull Request.
- Request a new topic creating a New issue with the enhancement tag.
- Find any kind of errors in the README and create a New issue with the details or fork the project and do a Pull Request.
- Suggest a better or more pythonic way for existing examples.
