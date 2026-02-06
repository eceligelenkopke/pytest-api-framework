import pytest
import logging as logger


from pyexpat.errors import messages

from grrmapitest.src.helpers.customers_helper import CustomerHelper
from grrmapitest.src.utilities.generic import generate_random_email_and_password
from build.lib.grrmapitest.src.dao.customers_dao import CustomersDAO
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_and_password():
    logger.info("TEST: Create a new customer with e-mail and password")
    rand_info = generate_random_email_and_password()
    logger.info(rand_info)
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_object = CustomerHelper()
    cust_api_info = cust_object.create_customer(email=email,password=password)
   # verify the e-mail and first name in response DONE
    assert cust_api_info['email'] == email, f"Create customer api returns wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '',f"Create customer api returned value for first_name" \
                                             "but it should be empty."

    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, (f"Create customer response 'id' not same as 'ID' in database"
                                   f"Email: {email}")

    # verify code status of the call DONE

    # verify the customer is created in db

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_with_existing_email(): ## Negative Test
    # get the existing user from db
    cust_dao = CustomersDAO()
    existing_customer = cust_dao.get_random_customer_from_db()
    existing_email = existing_customer[0]['user_email']

    # CALL THE API
    req_object = RequestsUtilities()
    payload = {"email": existing_email, "password":"password1"}
    cust_api_info = req_object.post(endpoint='customers',payload=payload,expected_status_code=400)


    assert cust_api_info['code'] == 'registration-error-email-exists', (f"Create customer with "
                                                                        f"existing user error 'code' is not correct."
                                                                        f"Expected registration-error-email-exists, "
                                                                        f"Actual: {cust_api_info['code']}")

    assert cust_api_info['message'] != (f'An account is already registered with your email address. Please log in or use a different email address.'
                                        f'Create customer with existing user error "message" is not correct.'
                                        f"Expected: An account is already registered with your email address. Please log in or use a different email address."
                                        f"Actual: {cust_api_info['message']}")

