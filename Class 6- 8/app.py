# from models import Address, session, User
from models import session, Course, StudentCourse, Student



# Clase - 6
## creating users - 
# user1 = User(name = "Jhon Doe", age=52)
# user2 = User(name = "Jane Smith", age=34)

# ## creating addresses - 
# address1 = Address(city = "New York", state="NY", zip_code="10001")
# address2 = Address(city = "Los Angeles", state="CA", zip_code="90001")
# address3 = Address(city = "Chicago", state="IL", zip_code="66001")

# ## associating users to addresses - 
# user1.addresses.extend([address1, address2])
# user2.addresses.append(address3)

# session.add(user1)
# session.add(user2)

# session.commit()
# # session.refresh()

# print(f"{user1.addresses = }")
# print(f"{user2.addresses = }")
# print(f"{address1.user = }")


# user1 = User(username = "Atal Bajpai 1")
# user2 = User(username = "Atal Bajpai 2")
# user3 = User(username = "Atal Bajpai 3")

# ## craete relationships - 
# user1.following.append(user2)
# user2.following.append(user3)
# user3.following.append(user1)

# ## adding users to session - 
# session.add_all([user1, user2, user3])
# session.commit()

# print(f"{user1.following = }")
# print(f"{user2.following = }")
# print(f"{user3.following = }")


################################################################
# MANY to MANY relationship - 
# math = Course(title='Mathematics')
# physics = Course(title='Physics')
# bill = Student(name = 'Bill', courses=[math, physics])
# rob = Student(name='Rob', courses=[math])

# session.add_all([math, physics, bill, rob])
# session.commit()


rob = session.query(Student).filter_by(name='Rob').first()
courses = [course.title for course in rob.courses]
print(f"Rob's courses : {', '.join(courses)}")


