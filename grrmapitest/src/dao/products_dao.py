import random
import string
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities
from grrmapitest.src.utilities.db_Utilities import DBUtility
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility


class ProductsDAO(object):
    def __init__(self):
        self.rs_utility = RequestsUtilities()
        self.db_utility = DBUtility()
        curs = self.db_utility.create_connection()
        self.woo_utility = WooAPIUtility()

    # Get a random product for test cases
    def get_a_random_product_from_db(self,qty=1):
        # Quantity given to use multiple times if required
        sql = 'SELECT * FROM local.wp_posts WHERE post_type = "product" LIMIT 5000;'
        rs_api = random.choice(self.rs_utility.get(endpoint='products', payload='id'))
        return rs_api,int(qty)

    # Get a product from API with a product ID
    def get_product_by_id(self,product_id):
        sql = f'SELECT * FROM local.wp_posts WHERE ID = {product_id} and post_type= "product";'
        rs_api = self.woo_utility.get(f"products/{product_id}")
        return self.db_utility.execute_select(rs_api)

    # Create a new random test product for test cases
    def create_a_random_product(self,domain=None,type=None):
        if not domain:
            domain = "/testproduct"
        if not type:
            type = "simple"
        rand_id = random.randint(100,999)
        rand_name_length = 10
        rand_name = "".join(random.choices(string.ascii_lowercase, k=rand_name_length))
        description = "This is a test product."
        post_product = "Product"
        regular_price = 1989
        price = 1989
        create_random_product = {
            "id":rand_id,
            "name":rand_name,
            "short_description":post_product,
            "description":description,
            "regular_price":regular_price,
            "price":price,
            "type":type

        }
        return create_random_product

    # Get the products from database with specific date
    def get_product_with_date(self,_date):
        sql = f'SELECT * FROM local.wp_posts WHERE post_type = "product" and post_date > "{_date}" LIMIT 10000;'
        return self.db_utility.execute_select(sql)

    # Get the product by sale prices
    def get_product_by_sale_price(self):
        sql =f'SELECT * FROM local.wp_postmeta WHERE meta_key = "_sale_price";'
        return self.db_utility.execute_select(sql)

    # Get all the products from database
    def _call_product_from_db(self,_product_id):
        sql = f'SELECT * FROM local.wp_posts WHERE post_type = "product" and ID = {_product_id};'
        rs_api = self.rs_utility.get(endpoint='products', payload=f'{_product_id}')
        return rs_api

    # Created Random String for Test Cases
    def create_random_string(self):
        rand_str_length = 5
        rand_str = "".join(random.choices(string.ascii_lowercase, k=rand_str_length))
        return rand_str
