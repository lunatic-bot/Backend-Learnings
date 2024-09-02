from sqlalchemy import  Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker


DATABASE_URL = "sqlite:///./learning.db"  # Path to your SQLite database file"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# class BaseModel(Base):
#     __abstract__ = True
#     __allow_unmapped__ = True

#     id = Column(Integer, primary_key=True)

# class Address(BaseModel):
#     __tablename__ = 'addresses'

#     city = Column(String)
#     state = Column(String)
#     zip_code = Column(Integer)
#     # user_id = Column(ForeignKey("users.id"))
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     # user = relationship("User", back_populates="addresses")
#     user: Mapped["User"] = relationship(back_populates="addresses")

#     def __repr__(self):
#         return f"<Address(id={self.id}, city={self.city})>"

# class User(BaseModel):
#     __tablename__ = "users"

#     name = Column(String)
#     age = Column(Integer)
#     # addresses = relationship(Address)
#     addresses: Mapped[list["Address"]] = relationship()

#     def __repr__(self):
#         return f"<User(id={self.id}, name={self.name})>"


# class User(Base):
#     __tablename__ = "users"
#     __allow_unmapped__ = True

#     id = Column(Integer, primary_key=True)

#     username = Column(String)
#     following_id = Column(Integer, ForeignKey('users.id'))
#     following = relationship('User', remote_side=[id], uselist=True)
    

#     def __repr__(self):
#         return f"<User(id={self.id}, name={self.username}), following={self.following})>"



## resolving circular dependency error - 
# class BaseModel(Base):
#     __abstract__ = True
#     __allow_unmapped__ = True

#     id = Column(Integer, primary_key=True)


# class FollowingAssociation(BaseModel):
#     __tablename__ = "following_association"
#     user_id = Column(Integer, ForeignKey("users.id"))
#     following_id = Column(Integer, ForeignKey("users.id"))

# class User(BaseModel):
#     __tablename__ = "users"

#     username = Column(String)
#     following = relationship('User', secondary='following_association',
#                              primaryjoin=("FollowingAssociation.user_id==User.id"),
#                              secondaryjoin=("FollowingAssociation.following_id==User.id"),
#                              )

#     def __repr__(self):
#         return f"<User(id={self.id}, name={self.username}), following={self.following})>"



# Base.metadata.create_all(engine)


################################################################################################
## Class - 8 
# MANY TO MANY Relationship - 


## Association table - 
# student_course_link = Table('student_course', Base.metadata,
#                             Column('student_id', Integer, ForeignKey('students.id')),
#                             Column('course_id', Integer, ForeignKey('courses.id'))
#                             )

# Also, we can write this table int his way - 
class StudentCourse(Base):
    __tablename__ = 'student_course'
    id = Column(Integer, primary_key= True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    course_id = Column('course_id', Integer, ForeignKey('courses.id'))
    # grade = Column(Integer)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key= True)
    name = Column(String)
    # courses = relationship("Course", secondary=student_course_link)
    courses = relationship("Course", secondary='student_course', back_populates='students')


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # students = relationship("Student", secondary=student_course_link)
    students = relationship("Student", secondary='student_course', back_populates='courses')

Base.metadata.create_all(engine)