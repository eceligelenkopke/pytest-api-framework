from grrmapitest.src.utilities.requestsUtility import RequestsUtilities
from grrmapitest.src.dao.products_dao import ProductsDAO
import logging as logger
class ProductsHelper(object):
    def __init__(self):
        self.request_utility = RequestsUtilities()

    # Get Product from API by ID
    def get_product_by_id(self,product_id):
        return self.request_utility.get(f"products/{product_id}")

    # Create Product in API
    def call_create_product(self,payload):
        return self.request_utility.post('products',payload=payload,expected_status_code=201)


