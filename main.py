from fastapi import FastAPI,Request
from mockdata import products
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

@app.get("/products/{product_id}")
def product_ids(product_id : int):
    for oproduct in products:
        if oproduct.get("id") == product_id:
            return oproduct
    return {
        "error": "product not found"
    }

@app.get("/greet")
def  greet(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return{"greet": f"Hello {query_params.get('name')} ,your age is {query_params.get('age')}"}