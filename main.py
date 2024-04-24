import warnings
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from getrate import getrate


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Send request to /rates/ with currency code(036, 051, 704, 978 etc.)"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.post("/rates/")
def rates(currency_code: str):
    return {"message": getrate(currency_code)}
