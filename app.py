#class - 2 : 
# import random
# from models import User, engine
# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)

# session = Session()

# user = User(name="Atal Bajpai", age=30)
# user_2 = User(name="Amit Singh", age=25)
# user_3 = User(name="Sivam Gaur", age=28)
# user_4 = User(name="Prachi Singh", age=31)

# session.add(user_2)
# session.add_all([user_3, user_4])
# session.commit()

# users = session.query(User).all()
# user = users[0]
# print(users[0])
# print(user.id)
# print(user.name)
# print(user.age)
# for user in users:
#     print({"user_id" : user.id, "name" : user.name, "age" : user.age})


# user = session.query(User).filter_by(id=1).all()
# print(user)


## Updating Records - 
# user = session.query(User).filter_by(id=1).one_or_none()
# user.name = "AtalB Bajpai"
# session.commit()


##delete -
# session.delete(user)
# session.commit()


## class 3 - 

import random
from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

# names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
# ages = [20, 21,22,23,25,27,30,35,60]

# for x in range(20):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)

# session.commit()

# order by - 
users = session.query(User).order_by(User.age, User.name).all()
for user in users:
    print({"user_id" : user.id, "name" : user.name, "age" : user.age})


