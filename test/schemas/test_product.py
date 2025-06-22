
import pytest
from store.schemas.product import ProductIn
from test.factories import product_data

def test_schemas_validated():
    data = product_data()
    product = ProductIn.model_validate(data)
    assert product.name == 'Iphone 14 pro Max'


def test_schemas_return_raise():
    data = {'name': 'Iphone 14 pro Max','quantity':10,'price':8.500,'status':True}
    product = ProductIn.model_validate(data)
