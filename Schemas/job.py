from pydantic import BaseModel

class JobCreate(BaseModel):
    title:str
    salary:int

class JobUpdate(BaseModel):
    title:Optional[str] = None
    salary:optional[int] = None
    
