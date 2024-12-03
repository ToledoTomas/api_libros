from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return str(v)
            

class Books(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    title: str
    autor: str
    page: int
    completed: bool = False
    
    class Config: 
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId:str}
        
        
class UpdateBooks(BaseModel):
    title: Optional[str] = None
    autor: Optional[str] = None
    page: Optional[int] = None
    completed: Optional[bool] = None
    
    class Config: 
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId:str} 