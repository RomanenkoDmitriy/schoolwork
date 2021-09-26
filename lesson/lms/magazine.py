
class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


class LessonCell:

    def __init__(self, student):
        self.student = student
        self.mark = input(f'Enter mark {student}: \t')


class Lesson:
    CELLS = []
    #date = datetime.datetime.now()

    def __init__(self, students, date):
        self.date = date
        for student in students:
          Lesson.CELLS.append(LessonCell(student))

    def __str__(self):
        output = []
        for les in Lesson.CELLS:
            output.append(f'{self.date} {les.student} {les.mark}')
        return str(output)



# class LessonCell:
#   def __init__(self, date, student, mark):
#     self.date = date
#     self.student = student
#     self.mark = mark
#
# class Lesson:
#
#   CELLS = []
#
#   def __init__(self, students):
#     for student in students:
#       pass
#


if __name__ == '__main__':
    student = Student('Vova', 'Pypkov')
    student1 = Student('Bob', 'Colin')
    students = [student, student1]
    lesson = Lesson(students, 25)
    print(lesson)




    #print(students[0], students[1], sep='\n')
    dict_student = student.__dict__
    #print(dict_student)
