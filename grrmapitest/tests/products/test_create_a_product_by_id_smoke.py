import pytest
from grrmapitest.src.utilities.generic import generate_random_string
from grrmapitest.src.helpers.products_helper import ProductsHelper
from grrmapitest.src.dao.products_dao import ProductsDAO

@pytest.mark.smoke
@pytest.mark.products
@pytest.mark.tcid26
# TEST CREATE A SIMPLE PRODUCT
def test_create_a_simple_product():
    # Generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] ="simple"
    payload['regular_price'] = "21.99"

    # Make the call
    rs_product = ProductsHelper().call_create_product(payload)

    # Verify the response is not empty
    assert rs_product,f"Create Product API response is empty. Payload: {payload}"
    assert rs_product['name']==payload['name'], (f"The name of created product and product in db does not mach."
                                                 f"Created Product name: {payload['name']}"
                                                 f"Database Product name: {rs_product['name']}")

    # Verify the product exists in db
    product_id = rs_product['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in db does not match" \
    f"title in api. DB:{db_product['post_title']}, API:{payload['name']}"