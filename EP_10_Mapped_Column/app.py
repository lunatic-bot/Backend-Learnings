from sqlalchemy import BIGINT, Column, ForeignKey, Integer, create_engine, String, Text
from sqlalchemy.orm import declarative_base, mapped_column, DeclarativeBase, Mapped, registry
# from time import perf_counter
from typing_extensions import Annotated

from typing import Optional

db_url = "sqlite:///database.db"

engine = create_engine(db_url, echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# str_20 = Annotated[str, 20]
# str_100 = Annotated[str, 100]

str_20 = Annotated[Optional[str], mapped_column(String(20))]
str_100 = Annotated[str, mapped_column(String(100))]


# Base = declarative_base()
class Base(DeclarativeBase):
    pass
    # registry = registry(
    #     type_annotation_map = {
    #     str_20: String(20),
    #     str_100: String(100),
    #     }
        
    # )

    # type_annotation_map = {
        #     int: BIGINT,
        # }
    

class UserLegasy(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True) # others can not be null
    # name: Mapped[Optional[str]] = mapped_column() # can have null now
    # name: Mapped[Optional[str]] # can have null now
    # age: Mapped[int] = mapped_column(nullable=True)

    first_name: Mapped[Optional[str_20]]
    lastname: Mapped[Optional[str_100]]


Base.metadata.create_all(engine)
