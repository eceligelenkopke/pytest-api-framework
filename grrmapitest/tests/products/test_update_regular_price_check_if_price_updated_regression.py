import pytest
import random
import pdb
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility
from grrmapitest.src.helpers.products_helper import ProductsHelper
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility
from grrmapitest.src.dao.products_dao import ProductsDAO

@pytest.mark.tcid61
def test_and_check_prices():
    # create product
    woo_utility = WooAPIUtility()
    products_dao = ProductsDAO()
    created_product = products_dao.get_a_random_product_from_db(qty=1)
    product_id=created_product[0]['id']
    reg_price = random.randint(1,9999)
    payload = {
        "regular_price":reg_price
    }

    # make the call
    rs_api = woo_utility.put(wc_endpoint=f'products/{product_id}',data=payload)


    # verify the changes in db
    check_changes = products_dao.get_product_by_id(product_id)
    pdb.set_trace()
    assert check_changes[0]['price'] == rs_api['regular_price'], (
        f"Test Check 'price' updated after updating 'regular_price' has failed. "
        f"Expected: {rs_api['regular_price']}, Actual: {check_changes[0]['price']}")


