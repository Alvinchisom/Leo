#schemas
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id : Optional[int]
    Name : str
    email : str
    password : str

class Update(BaseModel):
    Name : Optional[str] = None
    email : Optional[str] = None
    password : Optional[str] = None