from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

base = declarative_base()
class UserModel(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True,autoincrement = True)
    name = Column(String)
    age = Column(Integer)
    mother = Column(String)
    father = Column(String)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}