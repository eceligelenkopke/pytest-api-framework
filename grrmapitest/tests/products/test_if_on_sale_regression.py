import pytest
from grrmapitest.src.dao.products_dao import ProductsDAO
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility
@pytest.mark.products
@pytest.mark.regression
@pytest.mark.tcid63

def test_check_if_on_sale():
    # get a product from db
    p_dao = ProductsDAO()
    woo_util = WooAPIUtility()
    get_item = p_dao.get_a_random_product_from_db(1)
    item_id = get_item[0]['id']
    payload = {
        'sale_price':"150,67"
    }

    # bring value of its price and on sale
    sale_price = get_item[0]['sale_price']
    is_on_sale = get_item[0]['on_sale']
    # update product
    upd_product = woo_util.put(wc_endpoint=f'products/{item_id}',data=payload)


    # call product again
    get_upd_product = p_dao.get_product_by_id(item_id)

    # TEST INCOMPLETED (06.02.2026).
    # TO BE COMPLETED LATER.

