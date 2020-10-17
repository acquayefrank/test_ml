import pickle

import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel


class Train(BaseModel):
    X: list = []
    y: list = []


class Predict(BaseModel):
    X: list = []


app = FastAPI()


@app.get("/")
async def root():
    return {"docs": "/docs", "redoc": "/redoc", "ping": "/_ping", "train": "/train"}


@app.get("/_ping")
async def ping():
    return "pong"


@app.post("/train")
async def train(train: Train):
    train_dict = train.dict()
    print(train_dict.get("y", None))
    if train_dict.get("X", []) and train_dict.get("y", []):
        return {"success": True}
    else:
        return {"success": False}


@app.post("/predict")
async def predict(predict: Predict):
    predict_dict = predict.dict()
    X = predict_dict.get("X")
    data = [
        [
            "HouseStyle",
            "MSZoning",
            "GarageCars",
            "Street",
            "PavedDrive",
            "Utilities",
            "Neighborhood",
            "BldgType",
            "OverallQual",
            "OverallCond",
        ],
        X,
    ]
    column_names = data.pop(0)
    df = pd.DataFrame(data, columns=column_names)

    loaded_model = pickle.load(open("/app/api/model.sav", "rb"))
    result = loaded_model.predict(df)

    return {"success": True, "result": round(result[0],2)}
