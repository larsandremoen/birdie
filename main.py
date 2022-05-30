from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

import random

tueets = []


class Tueet(BaseModel):
    text: str


app = FastAPI()


@app.get("/get/tueets")
def get_tueets():

    # TODO open local file
    random_tueet = random.choice(tueets)
    return {"data": random_tueet}


@app.post("/post/tueet")
def read_root(tueet: Tueet):
    print("tueet ", tueet)

    tueets.append({"text": tueet.text, "id": len(tueets)})
    # TODO save locally
    return {"success": True}
