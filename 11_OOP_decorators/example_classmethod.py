class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_avg(cls, new_avg):
        cls.min_avg = new_avg

anna = Student('Anna', 'Kowalska', 22, 4.8)
jan = Student('Jan', 'Nowak', 23, 4.3)

print(anna.min_avg)
anna.set_avg(4.2)
print(anna.min_avg)
print(jan.min_avg)

