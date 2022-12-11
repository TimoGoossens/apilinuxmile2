from typing import Union

from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_client = MongoClient(host="tg-mongodb", port=27017, username="timo", password="abc123")
database = mongo_client['Milestone2']
collection = database["name"]




@app.get("/user")
def read_root():
    naam = collection.find({})[0]
    return {"name": naam["name"] }
