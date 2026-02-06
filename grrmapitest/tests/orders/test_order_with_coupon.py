import pytest
import pdb
from grrmapitest.src.helpers.orders_helper import OrdersHelper
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility
from grrmapitest.src.dao.products_dao import ProductsDAO
pytestmark = [pytest.mark.smoke,pytest.mark.orders]
@pytest.mark.tcid99

def test_discount_with_coupon():
    order_helper = OrdersHelper()
    products_dao = ProductsDAO()
    woo_utility = WooAPIUtility()

    # create an order
    first_created_order = order_helper.create_order()
    first_created_order_id = first_created_order['id']
    first_created_order_total = first_created_order['total']
    first_created_order_disc = first_created_order_total / 2
    rand_str = products_dao.create_random_string()
    # create a coupon
    created_coupon= {
        'code':rand_str,
        'amount':first_created_order_disc

    }
    # Send coupon to API
    rs_api_coupon = woo_utility.post(f"coupons",params=created_coupon,expected_status_code=201)
    send_coupon = {
        "coupon_lines":[
            {
                'code': rand_str,
                'amount': first_created_order_disc

            }
        ]
    }

    # make the call
    rs_api = woo_utility.put(wc_endpoint=f"orders/{first_created_order_id}",data=send_coupon)

    # check the values

    coupon_order_price = rs_api['total']
    coupon_order_total_disc=rs_api['discount_total']


    assert float(coupon_order_total_disc[0]) == float(first_created_order_total) - coupon_order_price ,(f"Test Order with coupon has failed."
                                                                                                        f"Price without Coupon: {first_created_order_total}"
                                                                                                        f"Discount Amount: {coupon_order_total_disc[0]} "
                                                                                                        f"Last Price: {coupon_order_price}")
