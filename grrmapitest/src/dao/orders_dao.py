from grrmapitest.src.utilities.db_Utilities import DBUtility
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities

class OrdersDAO(object):
    def __init__(self):
        self.db_utility = DBUtility() # Access to DB Properties

        curs = self.db_utility.create_connection() # Create Connection


    # Get the order item by id given
    def check_shopping_in_db(self,_id):
        sql = f'SELECT * FROM local.wp_woocommerce_order_items where order_item_id = {_id};'
        return self.db_utility.execute_select(sql)

    # Get a product with specific date
    def get_product_with_date(self,_date):
        sql = f'SELECT * FROM local.wp_posts WHERE post_type = "product" and post_date > "{_date}" LIMIT 10000;'
        return self.db_utility.execute_select(sql)

    # Get the product by id given
    def get_product_by_id(self,product_id):
        sql = f'SELECT * FROM local.wp_posts WHERE ID = {product_id};'
        return self.db_utility.execute_select(sql)




