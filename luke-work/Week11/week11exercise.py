class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def purr(self):
        print(f'{self.name} "pursss"')


    def meow(self):
        print(f'{self.name} "says meow"')

    def meet(self, other):
        if isinstance(other, Dog):
            print(f'{self.name} hises at {other.name}')
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name}says "barl"')

    def meet(self, other):
        if isinstance(other, Cat):
            print(f'{self.name} "barks at {other.name}')


cat = Cat('Whiskers', 3, 'red')

dog = Dog('rex', 65)


cat.meet(dog)


