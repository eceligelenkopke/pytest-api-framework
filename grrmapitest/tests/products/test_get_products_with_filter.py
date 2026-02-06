import pytest
from grrmapitest.src.helpers.products_helper import ProductsHelper
from datetime import datetime,timedelta
from grrmapitest.src.dao.products_dao import ProductsDAO
@pytest.mark.regression
class TestListProductsWithParameter(object): ##init__ verirsen test class olmaz.

    @pytest.mark.tcid51
    def test_list_products_with_parameter(self):
        #create data
        days_from_today = 30
        _after_created = datetime.now().replace(microsecond=0) - timedelta(days=days_from_today)
        after_created = _after_created.isoformat()


        # make the call
        payload = dict()
        payload['after'] = after_created
        #payload['per_page'] = 100p
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api,f"Empty response for 'list products with parameter'"


        # get data from db
        db_products = ProductsDAO().get_product_with_date(after_created)

        # verify response matches db

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff,f"List products with parameter. Product ids in response mismatch in db."