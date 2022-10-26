from qapages.domain.model import QAPage, Question, Answer

qapages_init = [
    QAPage(
        mainEntity=Question(
            name="What is Open Science?",
            text="What is Open Science?",
            answerCount=3,
            acceptedAnswer=[
                Answer(
                    text=(
                        "open science is…an inclusive construct that combines various "
                        "movements and practices aiming to make multilingual scientific "
                        "knowledge openly available, accessible and reusable for everyone, "
                        "to increase scientific collaborations and sharing of information "
                        "for the benefits of science and society, and to open the processes "
                        "of scientific knowledge creation, evaluation and communication to "
                        "societal actors beyond the traditional scientific community."
                    ),
                    url="https://en.unesco.org/science-sustainable-future/open-science/recommendation",
                ),
                Answer(
                    text=(
                        "Open Science is a social movement"
                        "…largely based on principles, "
                        "such as fairness, equality, inclusivity"
                        "…all about making science work better "
                        "so that it can address the world's challenges"
                        "…what the Web was developed for"
                        "…the movement to return science to its origins, "
                        "based on core values and principles that return "
                        "the practices of science to its humble and foundational origins."
                    ),
                    url="https://doi.org/10.5281/zenodo.3700646",
                ),
                Answer(
                    text=(
                        "Open Science is transparent and accessible knowledge that is "
                        "shared and developed through collaborative networks"
                    ),
                    url="https://doi.org/10.1016/j.jbusres.2017.12.043",
                ),
            ],
        )
    ),
    QAPage(
        mainEntity=Question(
            name="What are the main elements of Open Science?",
            text="What are the main elements of Open Science?",
            answerCount=2,
            acceptedAnswer=[
                Answer(
                    text=(
                        "The six principles of Open Science are: "
                        "Open methodology, Open source, Open data, "
                        "Open access, Open peer review, Open educational resources."
                    ),
                    url="https://forrt.org/glossary/open-science/",
                ),
                Answer(
                    text=(
                        "Key pillars: open scientific knowledge, "
                        "open science infrastructures, science communication, "
                        "open engagement of societal actors and "
                        "open dialogue with other knowledge systems "
                    ),
                    url="https://unesdoc.unesco.org/ark:/48223/pf0000379949.locale=en",
                ),
            ],
        )
    ),
    QAPage(
        mainEntity=Question(
            name="Does Open Science mean everything you do is open?",
            text="Does Open Science mean everything you do is open?",
            answerCount=2,
            acceptedAnswer=[
                Answer(
                    text=(
                        "It means that open is “opt-out”. That is, by default, "
                        "unless you have good reasons for something to not be open "
                        "(which happens!), make it open."
                    ),
                    url="",
                ),
                Answer(
                    text=(
                        "As open as possible, as closed as necessary and always secure."
                    ),
                    url="",
                ),
            ],
        )
    ),
    QAPage(
        mainEntity=Question(
            name="What is the difference between Open and FAIR?",
            text="What is the difference between Open and FAIR?",
            answerCount=2,
            acceptedAnswer=[
                Answer(
                    text=(
                        "FAIR means machine-actionable. Open means trying to have actionable "
                        "data accessible to as many humans (and their machines!) as practical."
                    ),
                    url="https://fairpoints.org/community",
                ),
                Answer(
                    text=(
                        "The FAIR principles for scientific data management and stewardship "
                        "are guidelines to improve the Findability, Accessibility, "
                        "Interoperability and Reusability of digital assets [1]."
                        "A dataset that is FAIR is not necessarily Open. "
                        'The phrase "as open as possible, as closed as necessary" [2] "'
                        '"is often used to describe the interaction between the principles.'
                    ),
                    url=[
                        "https://doi.org/10.1038/sdata.2016.18",
                        "https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-data-mgt_en.pdf",
                        "https://github.com/opensciency/OpenData",
                    ],
                ),
            ],
        )
    ),
    QAPage(
        mainEntity=Question(
            name="Where can I find FAIR data?",
            text="Where can I find FAIR data?",
            answerCount=2,
            acceptedAnswer=[
                Answer(
                    text=(
                        'A keyword here is "repository". "'
                        '"Or a phrase may be "research data repository". Or "dataset repository"'
                    ),
                    url="https://fairpoints.org/community",
                ),
                Answer(
                    text=(
                        "There are three major ways to find Data shared by researchers – "
                        "repository, web search, and literature search. "
                        "Repositories can be field specific or generic. A generalist repository"
                        "comparison chart [1] and comparative review of eight data repositories [2]"
                        "published by Dataverse provide comparisons "
                        "between a number of repositories."
                    ),
                    url=[
                        "https://zenodo.org/record/3946720#.YUKQ18RS-Uk",
                        "https://dataverse.org/blog/comparative-review-various-data-repositories",
                        "https://github.com/opensciency/OpenData",
                    ],
                ),
            ],
        )
    ),
    # QAPage(
    #     mainEntity=Question(
    #         name="",
    #         text="",
    #         answerCount=2,
    #         acceptedAnswer=[
    #             Answer(
    #                 text=(""),
    #                 url="",
    #             ),
    #             Answer(
    #                 text=(""),
    #                 url="",
    #             ),
    #         ],
    #     )
    # ),
]
