from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


DATABASE_URL = "sqlite:///./learning.db"  # Path to your SQLite database file"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)