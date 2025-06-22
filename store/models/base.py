from decimal import Decimal
from typing import Any
from pydantic import BaseModel, Field, UUID4, model_serializer
import uuid
from datetime import datetime
from bson import Decimal128

class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @model_serializer
    def set_model(self) -> dict[str,Any]:
        self_dict = dict(self)

        for key,value in self_dict.items():
            if isinstance(value,Decimal):
                self_dict[key] = Decimal128(str(value))
        
        return self_dict