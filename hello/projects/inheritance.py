class Parent():

    def print_last_name(self):
        print('Adeigbe')

class Child(Parent):

    def print_first_name(self):
        print('Mareez')
    def print_last_name(self):
        print('Ade')

mareez = Child()
mareez.print_first_name()
mareez.print_last_name()