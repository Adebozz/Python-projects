class Mario():
    def move(self):
        print('i am moving')

class Stream():
    def eat_shrom(self):
        print('Now i am big')

class BigMario(Mario, Stream):
    pass

on = BigMario()
on.move()
on.eat_shrom()