import pytest
import logging as logger

from grrmapitest.src.helpers.products_helper import ProductsHelper
from grrmapitest.src.utilities.requestsUtility import RequestsUtilities
from grrmapitest.src.dao.products_dao import ProductsDAO
from grrmapitest.src.helpers.products_helper import ProductsHelper
pytestmark = [pytest.mark.products, pytest.mark.smoke]
@pytest.mark.tcid24
def test_list_all_products():
    rs_utility = RequestsUtilities()
    rs_api = rs_utility.get(endpoint='products')
    import pdb; pdb.set_trace()
    assert rs_api,f"Get all products end point returned nothing."



@pytest.mark.tcid25
def test_get_a_product_by_id():
    #get a product from db
    rand_product = ProductsDAO().get_product_by_id(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    # make the call
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']

    assert db_name == api_name, (f"Get product by id returned wrong product. Id:{rand_product_id}"
                                 f"Db name: {db_name}, API Name: {api_name}")














#######################################################################################################################
# Alternative ways of me creating tests before watching the rest of the course.
#######################################################################################################################
#@pytest.mark.products
#@pytest.mark.tcid25
#def test_get_a_product_by_id():
#    pr_dao = ProductsDAO()
#    pr_utility = pr_dao.get_a_random_product_from_db()
#    assert pr_utility,"Get a product by payload id returned nothing."

#######################################################################################################################
# Alternative ways of me creating tests before watching the rest of the course.
#######################################################################################################################
#@pytest.mark.products
#@pytest.mark.products ################
#@pytest.mark.tcid25

#    logger.debug('GET API TEST: Get a Product by id')
#    rs_utility = RequestsUtilities()
#    rs_api = random.choice(rs_utility.get(endpoint='products', payload='id'))
#    import pdb; pdb.set_trace()
#    assert rs_api, "Get a product by customer id point returned nothing."

