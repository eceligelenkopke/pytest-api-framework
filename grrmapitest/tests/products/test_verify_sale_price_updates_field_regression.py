import pytest
from grrmapitest.src.dao.products_dao import ProductsDAO
from grrmapitest.src.utilities.wooAPIUtility import WooAPIUtility

@pytest.mark.tcid65
@pytest.mark.regression
@pytest.mark.product

def test_check_if_field():
    pd_dao = ProductsDAO()
    woo_uti = WooAPIUtility()

    # get a product from db
    new_product = pd_dao.get_a_random_product_from_db(1)
    new_product_id = new_product[0]['id']
    s_price = new_product[0]['sale_price']

    payload = {
        "sale_price":"145,89"
    }
    # make the call
    rs_api = woo_uti.put(wc_endpoint=f"products/{new_product_id}",data=payload)

    # get the product from db again
    updated_product = pd_dao._call_product_from_db(new_product_id)


    # verify the changes in db
    assert new_product[0]['sale_price'] == updated_product[0]['sale_price'],(f"TEST Verify sale price updates field\n"
                                                                             f"Expected:{new_product[0]['sale_price']}, Actual: {updated_product[0]['sale_price']}")

