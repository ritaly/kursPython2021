class Animals:
    def __init__(self):
        print("I'm animal")

    def eat(self):
        print('am am am')


class Stalocieplne(Animals):
    def wyleguj_sie(self):
        print('Leze na sloneczku')


class Dog(Stalocieplne):
    def __init__(self):
        print("I'm Dog")

    def eat(self):
        print('szybko wcinam karmę')

    def wyleguj_sie(self):
        print('-----')
        super().eat()
        print('Leze na kanapie')

    # --


dyzio = Dog()
dyzio.eat()
dyzio.wyleguj_sie()
