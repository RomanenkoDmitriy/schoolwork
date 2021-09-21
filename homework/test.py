class Asdf:

    def __init__(self):
        self.a = 21
        self.b = 'ew'

    def __str__(self):
        return f'{self.a} {self.b}'

class Dfdfgff(Asdf):

    def __init__(self):
        super()

    def print_aaaa(self):
        print(super(Asdf, self))


a = Asdf()
b = Dfdfgff()
b.print_aaaa()