from qapages.domain.model import Question, Answer, QAPage


def example_question():
    return Question(
        name="How many ounces are there in a pound?",
        text="How many ounces are there in a pound?",
        answerCount=0,
        acceptedAnswer=[],
        suggestedAnswer=[],
    )


def example_answer():
    Answer(
        text=(
            "Are you looking for ounces or fluid ounces? "
            "If you are looking for fluid ounces there are "
            "15.34 fluid ounces in a pound of water."
        ),
        url="https://example.com/question1#suggestedAnswer1",
    )


def test_question():
    example_question()


def test_answer():
    example_answer()
    Answer(
        text="this answer has two urls. [1][2]",
        url=["https://example.org/1", "https://example.org/2"],
    )


def test_qapage():
    q = example_question()
    q.suggestedAnswer.append(example_answer())
    QAPage(mainEntity=q)
