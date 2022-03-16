from fastapi import FastAPI
from pydantic import BaseModel


class Credentials(BaseModel):
    name: str = None
    type: str = None
    price: str = None


app = FastAPI(title="Products", version="0.0.1")


@app.get("/")
def home():
    return {"message": "Welcome to Paul Jor API"}


@app.get("/view")
def view_product(product: Credentials):
    return {
        "Product Name:": product.name,
        "Product Type:": product.type,
        "Product Price:": product.price
    }
