from typing import List

from fastapi import FastAPI, Depends
from jinja2 import Environment, PackageLoader, select_autoescape
from pymongo.database import Database as MongoDatabase
from starlette.responses import HTMLResponse

from qapages.adapters.repository import MongoQAPageRepository
from qapages.bootstrap import bootstrap
from qapages.config import get_mongo_db, HOST_URI_SCHEME_AUTHORITY
from qapages.domain.model import QAPage

app = FastAPI()

jinja_env = Environment(
    loader=PackageLoader("qapages", "entrypoints/templates"),
    autoescape=select_autoescape(),
)

qrepo: MongoQAPageRepository = bootstrap()


@app.get("/", response_model=List[QAPage], response_model_exclude_unset=True)
def read_root(mdb: MongoDatabase = Depends(get_mongo_db)):
    qapages = [QAPage(**d) for d in mdb["qapages"].find()]
    print(qapages[0].id_)
    return HTMLResponse(
        content=jinja_env.get_template("home.jinja2").render(
            qapages=qapages, summary_of_all_qapages=f"{len(qapages)} QAPages"
        ),
        status_code=200,
    )


@app.get("/QAPage/{id_}", response_model=QAPage, response_model_exclude_unset=True)
def read_item(id_: str, mdb: MongoDatabase = Depends(get_mongo_db)):
    qapage = QAPage(
        **mdb["qapages"].find_one({"@id": f"{HOST_URI_SCHEME_AUTHORITY}/QAPage/{id_}"})
    )
    question = qapage.mainEntity
    answers = question.suggestedAnswer + question.acceptedAnswer
    for a in answers:
        if not isinstance(a.url, list):
            a.url = [a.url]

    return HTMLResponse(
        content=jinja_env.get_template("qapage.jinja2").render(
            summary_of_all_qapage_answers=f'Answers to "{question.text}"',
            answers=answers,
            qapage_json=qapage.json(exclude_unset=True, indent=2),
        ),
        status_code=200,
    )
