from fastapi import FastAPI,Request
from removedfor.mockdata import products
from utils.db import Base,engine
from removedfor.dtos import ProductDTO


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def home():
    return  "WElcome to the fastapi backend"


@app.get("/hello")
def hello():
    return "this is hello"

@app.get("/products")
def product_data():
    return products

""" getting path params in fastapi"""
@app.get("/products/{product_id}")
def product_ids(product_id : int):
    for oproduct in products:
        if oproduct.get("id") == product_id:
            return oproduct
    return {
        "error": "product not found"
    }


""" seeing how to get query params in fastapi"""
@app.get("/greet")
def  greet(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return{"greet": f"Hello {query_params.get('name')} ,your age is {query_params.get('age')}"}

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    
    print(product_data.model_dump())
    products.append(product_data.model_dump())

    return{"status": "product created successfully","data":products}

@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO,product_id:int):
    for index,oneproduct in enumerate(products):
        if oneproduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status":"product updated successfully ","product":product_data}
    return {"error": "product not found"}

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,oneproduct in enumerate(products):
        if oneproduct.get("id") == product_id:
            deleted_product = products.pop(index)
            
            return {"status": "product deleted successfully","products":deleted_product}
    return {"error": "product not found"}