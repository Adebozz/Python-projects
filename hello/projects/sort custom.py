from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id= y
    def __repr__(self):
        return self.name + ":" + str(self.user_id)

users = [
    User
]