class Ade:

    def __init__(self):
        print('I am ade')
    def swim(self):
        print('I am swimming')

flipper = Ade()
flipper.swim()


class Enemy:

    def __init__(self, x) -> None:
        self.energy = x
    def get_energy(self):
        print(self.energy)

jesson = Enemy(5)
sam = Enemy(18)
gong = Enemy(100)

jesson.get_energy()
sam.get_energy()