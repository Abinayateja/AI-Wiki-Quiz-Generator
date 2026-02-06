from sqlalchemy import Column,Integer,String,Text,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.mysql import LONGTEXT


class Quiz(Base):

    __tablename__ = "quizzes"

    id = Column(Integer,primary_key=True,index=True)
    url = Column(String(500),unique=True)
    title = Column(String(500))
    summary = Column(Text)
    key_entities = Column(Text)
    sections = Column(Text)
    related_topics = Column(Text)
    raw_html = Column(LONGTEXT)

    questions = relationship("Question", back_populates="quiz")


class Question(Base):

    __tablename__ = "questions"

    id = Column(Integer,primary_key=True,index=True)

    quiz_id = Column(Integer,ForeignKey("quizzes.id"))

    question = Column(Text)
    options = Column(Text)
    answer = Column(String(255))
    difficulty = Column(String(50))
    explanation = Column(Text)

    quiz = relationship("Quiz", back_populates="questions")