import json

class Student:

    student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender', 'point']

    def __init__(self):
        self.student = {}

    def add_student(self):
        for field in self.student_fields:
            self.student[field] = input(f'Enter {field}: ')
            if field == 'age':
                try:
                    int(self.student['age'])
                except:
                    self.student['age'] = input('Enter age as number\t')


    def print_student(self, student):
        for field in student:
            print(field.replace('_', ' ').capitalize(), '\t', student[field])


class Group(Student):
    TEST_STUDENTS = [
        ['Mari', 'D', 'adadad@mail.ru', '19', 'Huston', 'F', 0],
        ['Jon', 's', 'hyhyhyhyh@mail.com', '21', 'London', 'M', 0],
        ['Andy', 'H', 'ggggggg@mail.com', 'sexteen', 'Citi', 'M', 0]
    ]

    def __init__(self, name):
        self.name = name
        self.STUDENTS = []

    def add_student_to_group(self, student):
        self.STUDENTS.append(student)

    def load_students(self):
        for test_student in self.TEST_STUDENTS:
            self.STUDENTS.append(dict(zip(self.student_fields, test_student)))

    def print_student_list(self):
        for student in self.STUDENTS:
            Student.print_student(self, student)
            print('<-------------------------------------------------------->')

    def dump_students(self):
        with open('data/student_data_oop.json', 'w') as file:
            json.dump(self.STUDENTS, file)

    def load_from_json(self, file_path='data/student_data_oop.json'):
        with open(file_path, 'r') as file:
            self.STUDENTS.extend(json.load(file))


if __name__ == '__main__':
    student = Student()
    group = Group('beetroot')
  #  print(student.student_fields)
  #  print(student.add_student())
    '''
    student.add_student()
    print('__________________________________________________________________________')
    print(student.print_student())
    print('=====================================')
    new_student = student.student
    print(new_student)
    
    group.add_student_to_group(new_student)
    students = group.STUDENTS
    print(students)
    '''


    #group.load_students()
    group.load_from_json()
    new_students = group.STUDENTS
    group.print_student_list()
    #group.dump_students()