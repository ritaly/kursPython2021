from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.counter = 0


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    code: Optional[str] = None
    tax: Optional[float] = None


@app.get("/")
def root():
    return {"message": "Hello World World World!"}


@app.get("/hello/{name}")
def hello_name(name: str):
    return f'Hello {name.capitalize()}'


@app.get("/counter")
def count():
    app.counter += 1
    return {"counter": app.counter}


@app.post("/products/")
def create_product(prod: Product):
    return prod
