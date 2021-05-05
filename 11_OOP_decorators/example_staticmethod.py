import datetime
import holidays


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

    @staticmethod
    def show_sth():
        return 'Obecnie rektorem jest Jon Snow'

    @staticmethod
    def academic_day(day):
        pl_holidays = holidays.Polish()
        if day in pl_holidays:
            return f'Nie ->Święto państwowe {pl_holidays.get(day)}'
        else:
            if day.weekday() == 5 or day.weekday() == 6:
                return 'Nie, weekend'
            else:
                return 'Tak'



anna = Student('Anna', 'Kowalska', 22, 4.8)
jan = Student('Jan', 'Nowak', 23, 4.3)
# text = Student.show_sth()
# print(text)

# today = datetime.date.today()
# print('Czy dzisiaj są zajęcia? ', Student.academic_day(today))

saturday = datetime.datetime.strptime('2019-01-06', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(saturday))

randomday = datetime.datetime.strptime('2019-02-06', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(randomday))

