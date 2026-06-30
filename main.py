from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "hello from store"


products = [
    Product(
        id=1,
        name="Phone",
        price=23000,
        description="Samsung A2",
        quantity=3
    ),
    Product(
        id=2,
        name="Laptop",
        price=24000,
        description="HP 640 G2",
        quantity=5
    )
]

@app.get("/products")
def get_all_product():
    return products

@app.get("/product/{id}")
def get_product_by_id(id : int):
    for product in products:
        if(product.id == id):
            return product
    return "product not found"    



@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Edit Successfully"
    
    return "No product Found"

@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return {"message": "Product Deleted"}

    return {"message": "Product Not Found"}