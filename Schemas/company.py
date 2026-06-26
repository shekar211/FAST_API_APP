from pydantic import BaseModel, Optional

class CompanyCreate(BaseModel):
    name:str
    location:str

class CompanyUpdate(BaseModel):
    name:Optional[str] = None
    location:Optional[str] = None
    
