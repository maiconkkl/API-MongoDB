from fastapi import FastAPI
import json
from bson.objectid import ObjectId
from database.Database import Database
from bson.json_util import dumps

app = FastAPI()


@app.get("/pessoas/")
def get_pessoas():
    database = Database()
    database_server = database.database_server()
    collection = database_server["Pessoas"]
    data = []
    cursor = collection.find({})
    x = 0
    try:
        for doc in cursor:
            data.append(json.loads(dumps(doc)))
            x += 1
    finally:
        database.close_connection()
    return data


@app.get("/pessoas/{uid}")
def read_pessoa(uid: str):
    database = Database()
    database_server = database.database_server()
    collection = database_server["Pessoas"]
    data = []
    try:
        cursor = collection.find_one({"_id": ObjectId(uid)})
        data.append(json.loads(dumps(cursor)))
    finally:
        database.close_connection()
    return data


@app.get("/movimentacoes/")
def movimentacoes():
    database = Database()
    database_server = database.database_server()
    collection = database_server["Movimentacoes"]
    data = []
    cursor = collection.find({})
    x = 0
    try:
        for doc in cursor:
            data.append(json.loads(dumps(doc)))
            x += 1
    finally:
        database.close_connection()
    return data


@app.post("/movimentacoes/{uid}")
def read_movimentacao(uid: str):
    pass