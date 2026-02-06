import pytest
from grrmapitest.src.dao.products_dao import ProductsDAO
from grrmapitest.src.helpers.orders_helper import OrdersHelper
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility
@pytest.mark.parametrize('discount_type',
                         [
    pytest.param('fixed_cart',marks=[pytest.mark.tcid67,pytest.mark.smoke]),
    pytest.param('fixed_product',marks=pytest.mark.tcid68),
    pytest.param('percent',marks=pytest.mark.tcid69),
                         ]
                )

def test_order_with_coupon_multiple(discount_type):
    order_helper = OrdersHelper()
    products_dao = ProductsDAO()
    woo_utility = WooAPIUtility()

    # create an order
    first_created_order = order_helper.create_order()
    first_created_order_id = first_created_order['id']
    # get the order variables needed
    first_created_order_price = first_created_order['line_items'][0]['price']
    first_created_order_total = first_created_order['total']
    
    # create a coupon
    rand_str = products_dao.create_random_string()
    created_coupon = {
        'code': rand_str,
        'amount': '7,5',
        "discount_type":discount_type
    }


    # apply the created coupon to the created order
    sent_coupon = {
        "coupon_lines": [
            {
                created_coupon
            }
        ]
    }

    #create coupon in API
    rs_api_coupon = woo_utility.post(f"coupons", params=created_coupon, expected_status_code=201)
    #apply coupon in API
    rs_api = woo_utility.put(wc_endpoint=f"orders/{first_created_order_id}",data=send_coupon)

    #get the variables after coupon applied
    coupon_order_price = rs_api['total']
    coupon_order_total_disc = rs_api['discount_total']

    #check if different discount_type coupons applied
    assert coupon_order_price != first_created_order_price, (f"Test order coupons with different discount types has failed."
                                                                                  f"The Amount of discount: {coupon_order_total_disc[0]}"
                                                                                  f"Discounted Price: {coupon_order_price}"
                                                                                                f"The Beginning Price: {first_created_order_price}"
                                                                                                )