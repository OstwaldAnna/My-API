from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model import *

connection = "sqlite:///bdshe4ka.db"
engine = create_engine(connection)
session = scoped_session(sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
))
class Query:
    def get_user(self) -> list[UserModel]:
        try:
            data = session.query(UserModel).all()
            return data
        except Exception as ex:
            return ex