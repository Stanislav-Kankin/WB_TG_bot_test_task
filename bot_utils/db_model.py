from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserDB(Base):
    __tablename__ = 'user_db_query'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer())
    time = Column(DateTime())
    article = Column(String())
