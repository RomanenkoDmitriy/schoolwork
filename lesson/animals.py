class Animal:
    paws = 4
    _tail = True
    ears = 2

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def voice(self):
        print('Bzzzzzzzzz!!!')

    @property
    def tail(self):
        if self._tail:
            return 'This animal has tail'
        else:
            return 'This animal has no tail'

    @tail.setter
    def tail(self, tail):
        if type(tail) is bool:
            self._tail = tail
        elif tail.lower() == 'yes':
            self._tail = True
        elif tail.lower() == 'no':
            self._tail = False


    #tail = property(get_tail, set_tail)


class Cat(Animal):

    @staticmethod
    def voice():
        print('MEOW!!!!!!!')


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class Dog(Animal):

    weight = 0
    TOTAL_COUNT = 0

    def __init__(self, name='Jak', weight=15):
        super().__init__(name)
        self.weight = weight
        Dog.TOTAL_COUNT += 1

    def voice(self):
        print('Bark! My name is {}'.format(self.name))

    def __eq__(self, other):
        if hasattr(other, 'weight'):
            return self.weight == other.weight
        else:
            return NotImplemented

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    @classmethod
    def get_total_count(cls):
        return cls.TOTAL_COUNT

    @classmethod
    def from_dict(cls, dict_data):
        obj = cls()
        for key in dict_data:
            setattr(obj, key, dict_data[key])
        return obj


class CatDog(Dog, Cat):

    def voice(self):
        print('Meow! Bark!')


if __name__ == '__main__':
    #dog1 = Dog('Tuzik', 25)
    #dog2 = Dog('Barbos', 30)
    #dog1 = Dog()
    #    print(dog1)
    #    print(dog1.weight)
    #dog_data = {'name': 'Joy', 'weight': 15}
   # dog2 = Dog.from_dict(dog_data)
   # print(dog2)
   # print(dog2.weight)
#    cat = Cat('Murzik')
#    print(dog1 == cat)
#    print(cat == dog1)

    bug = Animal('Bzzzz')
    print(bug)
    #bug.tail = 'No'
    print(bug.tail)

