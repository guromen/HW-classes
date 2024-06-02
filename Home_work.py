class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
           if course in lecturer.grades:
               lecturer.grades[course] += [grade]
           else:
               lecturer.grades[course] = [grade]
        else:
            return'Ошибка'
    
    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашнее задание: {self.mid_grade()}\n" \
              f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade()}'


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

#min, max студентов
m = max(student_1.mid_grade(),student_2.mid_grade())
n = min(student_1.mid_grade(),student_2.mid_grade())

print(f'Результат сравнения студентов(по средним оценкам за ДЗ):\n ' \
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1.mid_grade() < student_2.mid_grade()} ({m} > {n})')
print()

#min, max лекторов
a = max(lecturer_1.mid_grade(),lecturer_2.mid_grade())
b = min(lecturer_1.mid_grade(),lecturer_2.mid_grade())


print(f'Результат сравнения лекторов (по средним оценкам за лекции):\n ' \
      f'{lecturer_1.name} {lecturer_1.surname} > {lecturer_2.name} {lecturer_2.surname} = {lecturer_1.mid_grade() > lecturer_2.mid_grade()} ({a} > {b})')
print()