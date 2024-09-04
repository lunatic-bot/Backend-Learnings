from sqlalchemy import Column, ForeignKey, Integer, create_engine, String, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# Relationship loading techniques - 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', lazy='select', backref='user')

    def __repr__(self):
        return f'<User {self.name} >'
    
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'<Post {self.id} >'
    

Base.metadata.create_all(engine)


new_user = User(
    name = "Bob",
    posts = [
        Post(content = f"Thisn is the content for {x}")
        for x in range(1, 5)
    ]
)

session.add(new_user)
session.commit()
user = session.query(User).first()

print("Accessing user - ")
print(user)
print("accessing the post specifically.")
print(user.posts)