from pydantic import BaseModel 

class ProductDTO(BaseModel):
    id: int
    title:str
    count:int = 0
    price:int = 0
    