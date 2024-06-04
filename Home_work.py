class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def mid_grade(self):
        if not self.grades:
            return 0
        list_grade=[] 
        for v in self.grades.values():
            list_grade.extend(v)
        return round(float(sum([n for n in list_grade])/len(list_grade)), 1)

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашнее задание: {self.mid_grade()}\n" \
              f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
           if course in lecturer.grades:
               lecturer.grades[course] += [grade]
           else:
               lecturer.grades[course] = [grade]
        else:
            return'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
        return self.mid_grade() < other.mid_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
        return self.mid_grade() <= other.mid_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
        return self.mid_grade() == other.mid_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def mid_grade(self):
        if not self.grades:
            return 0
        list_grade=[]
        for v in self.grades.values():
           list_grade.extend(v)
        return sum([n for n in list_grade])/len(list_grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
        return self.mid_grade() < other.mid_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
        return self.mid_grade() <= other.mid_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
        return self.mid_grade() == other.mid_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]

            else: 
                student.grades[course] = [grade]
        else:
            return'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}\n')

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Petr', 'Petrov')
lecturer_2.courses_attached += ['Java']

rewiewer_1 = Reviewer('Some', 'Buddy')
rewiewer_1.courses_attached += ['Python']
rewiewer_1.courses_attached += ['Java']

rewiewer_1.__str__()

rewiewer_2 = Reviewer('Марь', 'Иванна')
rewiewer_2.courses_attached += ['Python']
rewiewer_2.courses_attached += ['Java']

student_1 = Student('Roman', 'Guguzin')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_1.finished_courses += ['Git']

student_2 = Student('Mikhail', 'Krug')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

#создал 3й экземпляр класса Student, чтобы отработать пример с рейтингом 
student_3 = Student('Arkadiy', 'Ukupnik')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Java', 10)
student_2.rate_hw(lecturer_2, 'Java', 5)
student_2.rate_hw(lecturer_2, 'Java', 6)

rewiewer_1.rate_hw(student_1, 'Python', 10)
rewiewer_1.rate_hw(student_1, 'Python', 9)
rewiewer_1.rate_hw(student_1, 'Python', 10)

rewiewer_2.rate_hw(student_2, 'Java', 8)
rewiewer_2.rate_hw(student_2, 'Java', 7)
rewiewer_2.rate_hw(student_2, 'Java', 9)

rewiewer_2.rate_hw(student_3, 'Python', 7)
rewiewer_2.rate_hw(student_3, 'Python', 6)
rewiewer_2.rate_hw(student_3, 'Python', 8)

print(f'Студенты:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()


print(f'Лекторы:\n\n{lecturer_1}\n\n{lecturer_2}')
print()

#min, max студентов
m = max(student_1.mid_grade(),student_2.mid_grade())
n = min(student_1.mid_grade(),student_2.mid_grade())

print(f'Результат сравнения студентов(по средним оценкам за ДЗ):\n' \
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2} (т.к. {m} > {n})\n' \
      f'{student_1.name} {student_1.surname} = {student_2.name} {student_2.surname} = {student_1 == student_2} (т.к. {m} > {n})\n' \
      f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname} = {student_1 > student_2} (т.к. {m} > {n})')
print()

#min, max лекторов
a = max(lecturer_1.mid_grade(),lecturer_2.mid_grade())
b = min(lecturer_1.mid_grade(),lecturer_2.mid_grade())


print(f'Результат сравнения лекторов (по средним оценкам за лекции):\n' \
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 < lecturer_2} (т.к. {a} > {b})\n' \
      f'{lecturer_1.name} {lecturer_1.surname} = {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 == lecturer_2} (т.к. {a} > {b})\n' \
      f'{lecturer_1.name} {lecturer_1.surname} > {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2} (т.к. {a} > {b})')
print()

student_list = [student_1 , student_2, student_3] 
lecturer_list = [lecturer_1, lecturer_2]

def student_rating(student_list, course_name):
    count_all = []
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            count_all.append(stud)
    return round(float(sum(n.mid_grade() for n in count_all)/len(count_all)), 1)

def lecturer_rating(lecturer_list, course_name):
    count_all = []
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            count_all.append(lect)
    return round(float(sum(n.mid_grade() for n in count_all)/(len(count_all))), 1)

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()