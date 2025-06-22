from motor.motor_asyncio import AsynIOMotorClient
from store.core.config import settings

class MongoClient:
    def __init__(self) -> None:
        self.client = AsynIOMotorClient = AsynIOMotorClient(settings.DATABASE_URL)
    
    def get(self) -> AsynIOMotorClient:
        return self.client
    

db_client = MongoClient()