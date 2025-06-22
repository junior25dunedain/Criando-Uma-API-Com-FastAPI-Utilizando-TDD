from typing import List
from uuid import UUID
from motor.motor_asyncio import AsynIOMotorClient, AsyncIOMotorDatabase
from store.core.exceptions import NotFoundException
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
import pymongo

class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsynIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection('products')
    
    async def create(self,body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        await self.collection.insert_one(product_model.model_dump())
        return ProductOut(**product_model.model_dump())
    
    async def get(self,id: UUID) -> ProductOut:
        result = await self.collection.find_one({'id':id})
        if not result:
            raise NotFoundException(message=f'produto não encontrado com o id {id}')
        
        return ProductOut(**result)
    
    async def query(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self,id: UUID,body: ProductUpdate) -> ProductUpdateOut:
        result = await self.collection.find_one_and_update(filter={'id':id},update={'$set':body.model_dump()},return_document=pymongo.ReturnDocument.AFTER)
        return ProductUpdateOut(**result)
    
    async def delete(self,id:UUID) -> bool:
        product = await self.collection.find_one({'id':id})
        if not product:
            raise NotFoundException(message=f'produto não encontrado com o id {id}')
        
        result = await self.collection.delete_one({'id':id})
        
        return True if result.deleted_count > 0 else False

usecase = ProductUsecase()