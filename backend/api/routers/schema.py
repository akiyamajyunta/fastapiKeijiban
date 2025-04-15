from datetime import datetime
from typing import List
from pydantic import BaseModel




class Thread(BaseModel):
    id: int
    user_name: str
    content: str


class GetResponse(BaseModel):
    results: List[Thread]





class CreateRequest(BaseModel):
    user_name: str = "ななし"
    content: str

class CreateResponse(BaseModel):
    id: int
    user_name: str
    content: str



class UpdateRequest(BaseModel):
    content: str


class UpdateResponse(BaseModel):
    id:int
    content:str





