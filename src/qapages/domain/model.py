from typing import Union, List, TYPE_CHECKING

from pydantic import Field, AnyUrl, HttpUrl
from pydantic_schemaorg.LearningResource import LearningResource
from pydantic_schemaorg.QAPage import QAPage as SDO_QAPage
from pydantic_schemaorg.Question import Question as SDO_Question
from pydantic_schemaorg.Answer import Answer as SDO_Answer


class TrainingMaterial(LearningResource):
    conformsTo: HttpUrl = Field(
        default="https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE",
        alias="dct:conformsTo",
        const=True,
    )
    description: Union[List[Union[str, "Text"]], str, "Text"]
    name: Union[List[Union[str, "Text"]], str, "Text"]
    keywords: Union[
        List[Union[AnyUrl, "URL", str, "Text", "DefinedTerm"]],
        AnyUrl,
        "URL",
        str,
        "Text",
        "DefinedTerm",
    ]


class Answer(SDO_Answer):
    text: Union[str, "Text"]
    url: Union[AnyUrl, "URL", List[Union[AnyUrl, "URL"]]]


class Question(SDO_Question):
    name: Union[str, "Text"]
    text: Union[str, "Text"]
    answerCount: Union[int, "Integer"]
    suggestedAnswer: List[Answer]
    acceptedAnswer: List[Answer]


class QAPage(SDO_QAPage):
    mainEntity: Question


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Integer import Integer
