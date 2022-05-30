import pickle
import random
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

tueets = []


class Tueet(BaseModel):
    text: str


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    global tueets

    try:
        with open("tueets", "rb") as fp:
            print("Loaded tueets")
            tueets = pickle.load(fp)
    except FileNotFoundError:
        pass


@app.get("/get/tueets")
def get_tueets():
    random_tueet = random.choice(tueets) if len(tueets) > 0 else None
    return {"data": random_tueet}


@app.post("/post/tueet")
def read_root(tueet: Tueet):
    print("tueet ", tueet)

    tueets.append({"text": tueet.text, "id": len(tueets)})
    with open("tueets", "wb") as filehandle:
        pickle.dump(tueets, filehandle)

    return {"success": True}
