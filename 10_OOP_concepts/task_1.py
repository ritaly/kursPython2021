class Animals:
    def __init__(self, animal_name):
        self.animal_name = animal_name
        print("Animals is one of the kingdoms in nature.")

    def feeding(self):
        print("Animals cannot be feed by photosynthesis.")


class Mammals(Animals):

    def __init__(self, animal_name):
        super().__init__(animal_name)
        self.animal_name = animal_name
        print(animal_name, "is a mammal.")


class Cat(Mammals):
    def __init__(self, cat_name):
        self.cat_name = cat_name
        print(cat_name, "is a wonderful cat.")
        super().__init__(cat_name)


class Dog(Mammals):
    def __init__(self, dog_name):
        self.dog_name = dog_name
        print(dog_name, "is a cute dog.")
        super().__init__(dog_name)


class Human(Mammals):
    def __init__(self, name):
        self.name = name
        print(name, "is a human.")
        super().feeding()


cat1 = Cat("Lolek")
dog1 = Dog("Sernik")
human1 = Human("Konstancja")