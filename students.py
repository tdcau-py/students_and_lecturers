class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg = self.__avg_grades_hw()
        courses_in_progress = ', '.join(course for course in self.courses_in_progress)
        finished_courses = ', '.join(course for course in self.finished_courses)

        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg:.1f}\n' \
               f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'

    def __lt__(self, other):
        return self < other

    def __le__(self, other):
        return self <= other

    def __gt__(self, other):
        return self > other

    def __ge__(self, other):
        return self >= other

    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return self != other

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __avg_grades_hw(self):
        self.avg = 0
        for grade in self.grades.values():
            self.avg += (sum(grade) / len(grade))

        return self.avg


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def __lt__(self, other):
        return self < other

    def __le__(self, other):
        return self <= other

    def __gt__(self, other):
        return self > other

    def __ge__(self, other):
        return self >= other

    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return self != other


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __str__(self):
        avg = self.__avg_grades_lecture()

        return Mentor.__str__(self) + f'\nСредняя оценка за лекции : {avg:.1f}'

    def __avg_grades_lecture(self):
        self.avg = 0
        for grade in self.grades.values():
            self.avg += (sum(grade) / len(grade))

        return self.avg


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


if __name__ == '__main__':
    student_1 = Student(name='Mikhail', surname='Ivanov', gender='Male')
    student_2 = Student(name='Elena', surname='Petrova', gender='Female')

    student_1.courses_in_progress += ['Python', 'Git']
    student_1.finished_courses += ['Basics of HTML and CSS']
    student_2.courses_in_progress += ['Python']
    student_2.finished_courses += ['Git']

    lecture_1 = Lecturer(name='Guido', surname='van Rossum')
    lecture_2 = Lecturer(name='Linus', surname='Torvalds')

    lecture_1.courses_attached += ['Python']
    lecture_2.courses_attached += ['Git']

    reviewer_1 = Reviewer(name='Monty', surname='Python')
    reviewer_2 = Reviewer(name='Pavel', surname='Borisov')

    reviewer_1.courses_attached += ['Python']
    reviewer_2.courses_attached += ['Python', 'Git']

    student_1.rate_lecture(lecture_1, 'Python', 10)
    student_1.rate_lecture(lecture_1, 'Python', 10)
    student_1.rate_lecture(lecture_2, 'Git', 10)

    student_2.rate_lecture(lecture_1, 'Python', 9)
    student_2.rate_lecture(lecture_2, 'Git', 9)

    reviewer_1.rate_hw(student_1, 'Python', 9)
    reviewer_2.rate_hw(student_1, 'Git', 10)
    reviewer_1.rate_hw(student_2, 'Python', 8)
    reviewer_1.rate_hw(student_2, 'Python', 9)

    print('Студенты:')
    print(student_1)
    print(f'\n{student_2}')
    print('-' * 20)
    print('Лекторы:')
    print(lecture_1)
    print(lecture_1.grades)
    print(f'\n{lecture_2}')
    print(lecture_2.grades)
    print('-' * 20)
    print('Проверяющие:')
    print(reviewer_1)
    print(f'\n{reviewer_2}')
