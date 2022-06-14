from sqlalchemy.orm import relationship

from fastapi.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
)

question_answers = Table(
    "user_forms",
    Base.metadata,
    Column("answer_id", ForeignKey("answers.id"), primary_key=True),
    Column("question_id", ForeignKey("questions.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)

    form_id = Column(Integer, ForeignKey("forms.id"))
    forms = relationship("Form", back_populates="users")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)

    questions = relationship(
        "Question", secondary=question_answers, back_populates="answers"
    )


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    questions = relationship(
        "Answer", secondary=question_answers, back_populates="questions"
    )
    answers = relationship("Answer", back_populates="questions")
    right_answers = relationship("Answer", back_populates="questions")


class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
