import datetime

from animals import Dog, Cat

class AnimalHotel:

    def __init__(self, visitors):
        self.date = datetime.datetime.now()
        if type(visitors) is list:
            self.visitors = visitors
        else:
            self.visitors = []

    def print_visitors(self):
        for visitor in self.visitors:
            print(visitor, end=', ')
        print()

    def add_visitor(self):
        while True:
            animal_type = input('What animal is it?\t')
            if animal_type.lower() == 'dog':
                self.visitors.append(Dog(
                    input('Name of the animal:\t')))
                break
            elif animal_type.lower() == 'cat':
                self.visitors.append(Cat(
                    input('Name of the animal:\t')))
                break
            else:
                continue

if __name__ == '__main__':
    dog = Dog('Tuzik')
    cat = Cat('Murzik')

    hotel = AnimalHotel([dog, cat])
    hotel.add_visitor()
    hotel.print_visitors()