from pydantic import BaseModel
from typing import List

class GenerateRequest(BaseModel):
    url: str


class QuestionOut(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: str
    explanation: str


class QuizResponse(BaseModel):
    id: int
    url: str
    title: str
    summary: str
    key_entities: dict
    sections: List[str]
    quiz: List[QuestionOut]
    related_topics: List[str]
