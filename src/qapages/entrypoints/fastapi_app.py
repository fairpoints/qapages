from typing import Union, List

from fastapi import FastAPI, Depends
from pymongo.database import Database as MongoDatabase

from qapages.adapters.repository import MongoQAPageRepository
from qapages.bootstrap import bootstrap
from qapages.config import get_mongo_db
from qapages.domain.model import QAPage

app = FastAPI()

qrepo: MongoQAPageRepository = bootstrap()


@app.get("/", response_model=List[QAPage], response_model_exclude_unset=True)
def read_root(mdb: MongoDatabase = Depends(get_mongo_db)):
    return list(mdb["qapages"].find())


@app.get("/QAPage/{id_}", response_model=QAPage, response_model_exclude_unset=True)
def read_item(id_: str, mdb: MongoDatabase = Depends(get_mongo_db)):
    return mdb["qapages"].find_one({"@id": f"https://fairpoints.org/QAPage/{id_}"})
