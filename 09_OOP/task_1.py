class Dog:
    def __init__(self, name, bred, color, age):
        self.name = name
        self.bred = bred
        self.color = color
        self.age = age

    def bark(self):
        return 'hau' * self.age

    def tail_wiggle(self):
        return self.name + " wiggle wiggle"


figa = Dog('Figa', 'kundelek', 'czarna podpalana', 2)
print(figa.name, figa.bred, figa.age)

print( figa.tail_wiggle())

