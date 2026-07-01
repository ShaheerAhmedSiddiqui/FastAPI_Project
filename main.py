from fastapi import Depends, FastAPI
from models import Product
from database import SessionLocal, engine
import database_model
from sqlalchemy.orm import Session

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def db_init():
    db = SessionLocal()

    count = db.query(database_model.Product).count

    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))

        db.commit()
db_init()   

@app.get("/products")
def get_all_product(db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).all()
    return db_product

@app.get("/product/{id}")
def get_product_by_id(id : int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"    



@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()

    return product

@app.put("/product")
def update_product(id: int, product: Product,  db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.quantity = product.quantity
        db_product.price = product.price
        db.commit()
        return "Product Edit Successfully"
    else:
        return "No product Found"

@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted"
    else:    
        return {"message": "Product Not Found"}