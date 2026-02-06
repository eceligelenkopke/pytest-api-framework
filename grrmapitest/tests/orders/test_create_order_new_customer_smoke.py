import pytest
import random
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities
from grrmapitest.src.dao.products_dao import ProductsDAO
from grrmapitest.src.helpers.orders_helper import OrdersHelper
from grrmapitest.src.dao.orders_dao import OrdersDAO
from grrmapitest.src.helpers.customers_helper import CustomerHelper
from grrmapitest.src.utilities.generic import generate_random_email_and_password
@pytest.mark.smoke
@pytest.mark.order
@pytest.mark.tcid49

def test_create_order_with_new_customer():
    # create helper objects
    order_dao = OrdersDAO()
    products_dao = ProductsDAO()
    order_helper = OrdersHelper()
    customer_helper = CustomerHelper()
    # get product from db
    rand_product = products_dao.get_a_random_product_from_db(1)
    product_id = rand_product[0]['id']

    # make the call
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']
    info= {"line_items": [
    {
      "product_id": product_id,
      "quantity": 1
    }
            ],
    "customer_id":customer_id
    }
    order_json = order_helper.create_order(additional_args=info)
    # verify response
    assert order_json, f"Create order response is empty."
    assert order_json['customer_id'] == customer_id, (f"The used customer account for ordering is not a match with the fresh created customer id. "
                                            f"Expected:{customer_id}, Actual: {order_json['customer_id']}")
    assert len(order_json['line_items']) == 1, f"Expected only one 1 item in order, but found: {len(order_json['line_items'])}"
    assert order_json['order_key'], f"Order key seems empty though it should return the key itself. What is Found: {order_json['order key']} ....till here."

