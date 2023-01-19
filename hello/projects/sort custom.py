from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id= y
    def __repr__(self):
        return self.name + ":" + str(self.user_id)

users = [
    User('Bucky', 43),
    User('Saly', 5),
    User('Mareez', 61),
    User('Adeolu', 2),
    User('Ife', 15),
    User('Amaka', 9)
]

for User in users:
    print(User)

print('-----')
for User in sorted(users, key=attrgetter('name')):
    print(User)