import json

class Student:

    student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender', 'point']

    def __init__(self):
        self. first_name = input(f'Enter {self.student_fields[0].replace("_", " ").capitalize()}:\t')
        self. last_name = input(f'Enter {self.student_fields[1].replace("_", " ").capitalize()}:\t')
        self. email = input(f'Enter {self.student_fields[2].replace("_", " ").capitalize()}:\t')
        self.age = input(f'Enter {self.student_fields[3].replace("_", " ").capitalize()}:\t')
        self. address = input(f'Enter {self.student_fields[4].replace("_", " ").capitalize()}:\t')
        self.gender = input(f'Enter {self.student_fields[5].replace("_", " ").capitalize()}:\t')
        self.point = input(f'Enter {self.student_fields[6].replace("_", " ").capitalize()}:\t')


    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


class Group(Student):
    '''
    _TEST_STUDENTS = [
        ['Mari', 'D', 'adadad@mail.ru', '19', 'Huston', 'F', 0],
        ['Jon', 's', 'hyhyhyhyh@mail.com', '21', 'London', 'M', 0],
        ['Andy', 'H', 'ggggggg@mail.com', 'sexteen', 'Citi', 'M', 0]
    ]
    '''

    def __init__(self, name):
        super()
        self.name = name
        self.STUDENTS = []

    def add_student_to_group(self, student):
        self.STUDENTS.append(student)

    '''
    def load_students(self):
        for test_student in self._TEST_STUDENTS:
            self.STUDENTS.append(dict(zip(self.student_fields, test_student)))
    '''

    def print_student_list(self):
        for student in self.STUDENTS:
            print(student)
            print('<-------------------------------------------------------->')
    '''
    def dump_students(self):
        with open('data/student_data_oop.json', 'w') as file:
            json.dump(self.STUDENTS, file)

    def load_from_json(self, file_path='data/student_data_oop.json'):
        with open(file_path, 'r') as file:
            self.STUDENTS.extend(json.load(file))
    '''

if __name__ == '__main__':
    student1 = Student()
    student2 = Student()
    #print(student)
    print('-------------------------------------------')
    group = Group('Beetroot')
    group.add_student_to_group(student1)
    group.add_student_to_group(student2)
    group.print_student_list()
    #group.load_students()
    #group.load_from_json()
    #new_students = group.STUDENTS

    #group.dump_students()
    #student.print_student(student.student)