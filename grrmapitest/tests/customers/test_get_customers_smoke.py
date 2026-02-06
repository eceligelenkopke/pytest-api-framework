
import logging as logger
import pytest
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities
pytestmark = [pytest.mark.products, pytest.mark.smoke]
def test_get_all_customers():
    rs_utility = RequestsUtilities()
    rs_api = rs_utility.get('customers')
    assert rs_api, f"Response of list all customers are empty."
