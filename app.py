from models import Address, session, User


# Clase - 6
## creating users - 
user1 = User(name = "Jhon Doe", age=52)
user2 = User(name = "Jane Smith", age=34)

## creating addresses - 
address1 = Address(city = "New York", state="NY", zip_code="10001")
address2 = Address(city = "Los Angeles", state="CA", zip_code="90001")
address3 = Address(city = "Chicago", state="IL", zip_code="66001")

## associating users to addresses - 
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

session.add(user1)
session.add(user2)

session.commit()
# session.refresh()

print(f"{user1.addresses = }")
print(f"{user2.addresses = }")
print(f"{address1.user = }")


