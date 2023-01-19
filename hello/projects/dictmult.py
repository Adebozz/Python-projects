from operator import itemgetter

users = [
    {'fname': 'Mariam', 'lname': 'Olabode'},
    {'fname': 'tope', 'lname': 'Olawale'},
    {'fname': 'feyi', 'lname': 'Olarewaju'},
    {'fname': 'Rofiya', 'lname': 'Oyekola'},
    {'fname': 'Aishat', 'lname': 'Adebayo'},
    {'fname': 'Mariam', 'lname': 'Adeolu'},
]

for x in sorted(users, key=itemgetter('fname')):
    for y in sorted(users, key=itemgetter('lname')):
        print(y)
