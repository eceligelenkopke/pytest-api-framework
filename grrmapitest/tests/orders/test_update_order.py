import pytest
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility
from grrmapitest.src.helpers.orders_helper import OrdersHelper
from grrmapitest.src.utilities.generic import generate_random_string
pytestmark = [pytest.mark.orders,pytest.mark.regression]

@pytest.mark.parametrize("new_status",[
    pytest.param('cancelled',marks=[pytest.mark.tcid55,pytest.mark.smoke]),
    pytest.param('completed',marks=pytest.mark.tcid56),
    pytest.param('on-hold',marks=pytest.mark.tcid57) ## bir noktaya birden fazla değer göndermek ve ayrı ayrı test etmek için.


])
def test_update_order_status(new_status):
    order_helper = OrdersHelper()

    #create new order
    order_json = order_helper.create_order()
    current_status = order_json['status']
    assert current_status != new_status, (f"Current status of order is already {new_status}. "
                                          f"Unable to run the test.")
    # change the order status // UPDATE
    order_id = order_json['id']
    payload = {"status":new_status}
    order_helper.call_update_an_order(order_id,payload)


    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    #verify the changes
    assert new_order_info['status'] == new_status, (f"Updated order status to '{new_status}' "
                                                   f"But order is still {new_order_info['status']}")

@pytest.mark.tcid58
def test_update_order_status_to_random_str():
    order_helper = OrdersHelper()

    # create new order
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # change the order status // UPDATE
    new_status = "abcdefgghfgh"
    payload = {"status": new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_id}',data=payload,expected_status_code=400)

    #verify
    assert rs_api['code'] == 'rest_invalid_param',(f"It returned the wrong code."
                                                   f"Expected: rest_invalid_param, Actual: {rs_api['code']}")
    assert rs_api['message'] == 'Invalid parameter(s): status', (f"It returned the wrong message."
                                                    f"Expected: rest_invalid_message, Actual: {rs_api['message']}")


@pytest.mark.tcid59
def test_update_order_customer_note():
    # Create New Order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']
    rand_str = generate_random_string(40)


    #UPDATE The Order
    payload = {"customer_note": rand_str}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    assert new_order_info['customer_note'] == rand_str, (f"Expected customer note: {rand_str}"
                                                         f"Actual customer note in db: {new_order_info['customer_note']}")
