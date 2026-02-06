import pytest
import random
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities
from grrmapitest.src.dao.products_dao import ProductsDAO
from grrmapitest.src.helpers.orders_helper import OrdersHelper
from grrmapitest.src.dao.orders_dao import OrdersDAO

@pytest.fixture(scope='module') # To create a setup. Cannot be reached unless done.
def my_setup():
    product_dao=ProductsDAO()
    rand_product = product_dao.get_a_random_product_from_db(1)
    product_id = rand_product[0]['id']
    info = {"product_id":product_id}
    return info
@pytest.mark.smoke
@pytest.mark.order
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_setup):
    order_dao = OrdersDAO()
    products_dao = ProductsDAO()
    order_helper = OrdersHelper()

    # get product from db
    product_id = my_setup['product_id']

    # make the call
    info= {"line_items": [
    {
      "product_id": product_id,
      "quantity": 1
    }
            ]}
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    assert order_json, f"Create order response is empty."
    assert order_json['customer_id'] == 0, (f"The used customer account for ordering is not guest. "
                                            f"Expected:0, Actual: {order_json['customer_id']}")
    assert len(order_json['line_items']) == 1, f"Expected only one 1 item in order, but found: {len(order_json['line_items'])}"
    assert order_json['order_key'], f"Order key seems empty though it should return the key itself. What is Found: {order_json['order key']} ....till here."


    #verify db
    order_id = order_json['id']
    line_info = order_dao.check_shopping_in_db(order_id)

    assert line_info,f"Create order, line item not found in db. Order id: {order_id}"


    # Setup is for being able to use the same product for each test in this file.


