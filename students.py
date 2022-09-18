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

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
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


class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        avg = 0
        for grade in self.grades.values():
            avg += (sum(grade) / len(grade))

        return Mentor.__str__(self) + f'\nСредняя оценка за лекции : {avg:.1f}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

lecture_1 = Lecturer('Bryan', 'Smith')
lecture_1.courses_attached.append('Python')

best_student.rate_lecture(lecture_1, 'Python', 7)
best_student.rate_lecture(lecture_1, 'Python', 10)
best_student.rate_lecture(lecture_1, 'Python', 9)

print(lecture_1)

print(cool_reviewer)

print(best_student)
