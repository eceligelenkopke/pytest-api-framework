import pytest
from grrmapitest.src.dao.products_dao import ProductsDAO
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility
@pytest.mark.parametrize('regular_price',
    [
        pytest.param(values = 1453,marks=pytest.mark.tcid99),
        pytest.param(values = 1989, marks=pytest.mark.tcid100)
     ]
)

def test_update_price(regular_price):
    #create a product
    product_dao = ProductsDAO()
    woo_util = WooAPIUtility()
    created_product = product_dao.create_a_random_product()
    created_product_price = created_product["regular_price"]
    created_product_id = created_product['id']

    #make the call
    payload = {'regular_price' :regular_price }
    rs_api = woo_util.put(wc_endpoint={f'products/{created_product_id}'},payload=payload)
    updated_price_api = rs_api['regular_price']

    #check changes
    get_new_price = woo_util.get(wc_endpoint={f'products/{created_product_id}'})
    updated_price = get_new_price['regular_price']

    assert updated_price == regular_price,(f"Test update price has failed. "
                                           f"Expected:{regular_price}, "
                                           f"Actual:{updated_price}")

    assert updated_price != created_product_price,(f"Test update price has failed."
                                                   f"Expected: {updated_price}, Actual: {created_product_price}")

    assert updated_price_api == updated_price, (f"Test update price has failed."
                                                f"The updated price in api call is: {updated_price_api}, "
                                                f"The updated price should be: {updated_price}")