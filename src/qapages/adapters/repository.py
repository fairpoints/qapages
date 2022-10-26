import abc
from typing import Set
from qapages.domain import model

from pymongo.database import Database as MongoDatabase

from qapages.domain.model import id_localpart_from_str


class QAPageRepository(abc.ABC):
    def __init__(self):
        self.seen: Set[model.Question] = set()

    def add_qapage(self, qapage: model.QAPage):
        self._add_qapage(qapage)
        self.seen.add(qapage.id_)

    def add_answer(self, qapage: model.QAPage, answer: model.Answer):
        self._add_answer(qapage, answer)
        self.seen.add(qapage.id_)

    def get(self, qapage_id: str) -> model.QAPage:
        qapage = self._get(qapage_id)
        if qapage:
            self.seen.add(qapage.id_)
        return qapage

    @abc.abstractmethod
    def _add_qapage(self, qapage: model.QAPage):
        raise NotImplementedError

    @abc.abstractmethod
    def _add_answer(self, qapage: model.QAPage, answer: model.Answer):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, qapage_id: str) -> model.QAPage:
        raise NotImplementedError


class MongoQAPageRepository(QAPageRepository):
    def __init__(self, mdb: MongoDatabase):
        super().__init__()
        self.mdb = mdb
        self.qapages = mdb["qapages"]

    def _add_qapage(self, qapage: model.QAPage):
        if not self.qapages.find_one({"@id": qapage.id_}):
            self.qapages.insert_one(qapage.dict())

    def _add_answer(self, qapage: model.QAPage, answer: model.Answer):
        self.qapages.update_one(
            {"@id": qapage.id_},
            {"$push": {qapage.mainEntity.suggestedAnswer: answer.dict()}},
        )

    def _get(self, qapage_id: str) -> model.QAPage:
        return model.QAPage(**self.qapages.find_one({"@id": qapage_id}))
