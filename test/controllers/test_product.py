
from typing import List
from fastapi import status
from tests.factories import product_data
import pytest

async def test_controller_create_should_return_success(client,products_url):
    response = await client.post(products_url,json=product_data())
    content = response.json()
    del content['created_at']
    del content['update_at']
    del content['id']

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {'name': 'Iphone 14 Pro Max','quantity':10,'price':'8.500','status':True}


async def test_controller_get_should_return_success(client,products_url,product_inserted):
    response = await client.get(f"{products_url}{product_inserted.id}")
    content = response.json()
    del content['created_at']
    del content['update_at']
    
    assert response.status_code == status.HTTP_200_OK
    assert content == {'id': str(product_inserted.id),'name': 'Iphone 14 Pro Max','quantity':10,'price':'8.500','status':True}


async def test_controller_get_should_return_not_found(client,products_url):
    response = await client.get(f"{products_url}kljsklfjw3r3wlnkn")

    assert response.status_code == status.HTTP_404_NOT_FOUND   
    assert response.json() == {'detail':"product not found: kljsklfjw3r3wlnkn"}

@pytest.mark.usefixtures('products_inserted')
async def test_controller_query_should_return_success(client,products_url):
    response = await client.get(products_url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(),List)
    assert len(response.json()) > 1


async def test_controller_patch_should_return_success(client,products_url,product_inserted):
    response = await client.patch(f"{products_url}{product_inserted.id}",json={'price':'10.000'})
    content = response.json()
    del content['created_at']
    del content['update_at']
    
    assert response.status_code == status.HTTP_200_OK
    assert content == {'id': str(product_inserted.id),'name': 'Iphone 14 Pro Max','quantity':10,'price':'10.000','status':True}

async def test_controller_delete_should_return_no_content(client,products_url,product_inserted):
        response = await client.delete(f"{products_url}{product_inserted.id}",json={'price':'10.000'})
        assert response.status_code == status.HTTP_204_NO_CONTENT

async def test_controller_delete_should_return_not_found(client,products_url,product_inserted):
    response = await client.delete(f"{products_url}kljsklfjw3r3wlnkn")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail':"product not found: kljsklfjw3r3wlnkn"}
