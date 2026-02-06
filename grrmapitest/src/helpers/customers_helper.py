from grrmapitest.src.utilities.credentialsUtility import CredentialsUtility
from grrmapitest.src.utilities.generic import generate_random_email_and_password
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities
class CustomerHelper(object):
    def __init__(self):
        self.request_utility = RequestsUtilities() # Access API

    # Function: Create a New User
    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'password1'

        # Create the Payload
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        # Create the User and Check the Status Code
        create_user_json = self.request_utility.post('customers',payload=payload,expected_status_code=201)
        return create_user_json
