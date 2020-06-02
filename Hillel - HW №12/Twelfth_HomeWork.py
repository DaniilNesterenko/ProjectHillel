# Task 1
# 1. Реализовать класс цифрового счетчика. Обеспечьте возможность установки максимального и минимального значений,
# увеличения счетчика на 1, возвращения текущего значения.
print('Task №1')
print()

class Counter:

    def __init__(self, min_value, max_value, current_value, increment=1):
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = current_value
        self.increment = increment

    def increase_value(self):
        self.current_value += self.increment

    def reset(self):
        if self.current_value > self.max_value:
            self.current_value -= self.max_value
        else:
            self.current_value = self.min_value

    def get_current(self):
        return self.current_value

    def return_maximum(self):
        return self.max_value

counter_tester = Counter(0, 25, 0)

for _ in range(30):
    counter_tester.increase_value()

    if counter_tester.get_current() >= counter_tester.return_maximum():
        counter_tester.reset()

print(counter_tester.get_current())
print()

# Task 2
# Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов `Student`
# также реализованного в виде соответствующего класса. В классах реализовать необходимай набор атрибутов
# (Например класс `Student` должен иметь атрибуты `name`, `age`, `grades`), а так же необходимый набор методов
# экземпляра для работы с этими экземплярами.
print('Task №2')
print()

class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def name_edit(self, name):
        self.name = name

    def age_edit(self, age):
        self.age = age

    def grades_edit(self, grades):
        self.grades = grades

    def display_student_info(self):
        print('Имя студента:', self.name)
        print('Возраст студента:', self.age)
        print('Список оценок студента:', self.grades )
        print()



class Group:

    def __init__(self, group_name, list_of_students):
        self.group_name = group_name
        self.list_of_students = list_of_students

    def group_name_edit(self, group_name):
        self.group_name = group_name

    def add_student_to_group(self, student):
        self.list_of_students.append(student)

    def delete_student_from_group(self, student):
        self.list_of_students.remove(student)

    def display_group(self):
        print('Название группы:', self.group_name)

from random import randint

student_1 = Student('Louis', 20, [randint(1, 10) for _ in range(5)])
student_2 = Student('Kate', 22, [randint(1, 10) for _ in range(5)])
student_3 = Student('Romain', 21, [randint(1, 10) for _ in range(5)])
student_4 = Student('Sebastien', 24, [randint(1, 10) for _ in range(5)])
student_5 = Student('Thina', 19, [randint(1, 10) for _ in range(5)])

student_5.display_student_info()

student_1.display_student_info()

student_1.name_edit('Patrick')
student_1.age_edit(18)
student_1.grades_edit([randint(2, 7) for _ in range(5)])
student_1.display_student_info()


group_1 = Group('Dream Team', [])
group_2 = Group('One Team', [])

group_1.add_student_to_group(student_1)
group_1.add_student_to_group(student_3)

group_2.add_student_to_group(student_2)
group_2.add_student_to_group(student_4)
group_2.add_student_to_group(student_5)

group_1.display_group()
print('Студенты группы:', [student.name for student in group_1.list_of_students])
print()

group_2.display_group()
print('Студенты группы:', [student.name for student in group_2.list_of_students])
print()

group_1.delete_student_from_group(student_1)
group_2.delete_student_from_group(student_5)

group_1.add_student_to_group(student_5)
group_2.add_student_to_group(student_1)

group_1.display_group()
print('Студенты группы:', [student.name for student in group_1.list_of_students])
print()

group_2.display_group()
print('Студенты группы:', [student.name for student in group_2.list_of_students])
print()