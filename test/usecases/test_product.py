from typing import List
from uuid import UUID
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import usecase
import pytest 


async def test_usecases_should_return_success(product_in):
    result = await usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"


async def test_usecases_get_should_return_success(product_inserted):
    result = await usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"

async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await usecase.get(id=UUID('dgdçlgrl'))
    assert err.value.message == 'produto não encontrado com o id'

@pytest.mark.usefixtures('products_inserted')
async def test_usecases_query_should_return_success():
    result = await usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_inserted,product_up):
    product_up.price = '7.500'
    result = await usecase.update(id=product_inserted.id,body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    result = await usecase.delete(id=product_inserted.id)
    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await usecase.delete(id=UUID('dgdçlgrl'))
    assert err.value.message == 'produto não encontrado com o id'

