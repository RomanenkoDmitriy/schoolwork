
class Student:

    #student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender', 'point']
    TOTAL_STUDENT = []

    def __init__(self, first_name, last_name, email, age, address, gender, point=0):
        self. first_name = first_name
        self. last_name = last_name
        self. email = email
        self.age = age
        self. address = address
        self.gender = gender
        self.point = point
        Student.TOTAL_STUDENT.append({self.first_name: self})


    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def __eq__(self, other):
        return self.age == other.age

    @classmethod
    def print_total_student(cls):
        print(cls.TOTAL_STUDENT)

    @classmethod
    def add_student_dict(cls, dict_student):
        obj = cls(first_name='', last_name='', email='', age=0, address='', gender='', point=0)
        for key in dict_student:
            setattr(obj, key, dict_student[key])
        return obj


class Group(Student):

    def __init__(self, name):
        super()
        self.name = name
        self.STUDENTS = []

    def add_student_to_group(self, student):
        self.STUDENTS.append(student)

    def print_student_list(self):
        for student in self.STUDENTS:
            print(student)
            print('<-------------------------------------------------------->')



#Обьект student1 создаетца и у него есть все аргументы но метод print_total_student почемуто не находит first_name


if __name__ == '__main__':
    student = Student('Mari', 'Boow', 'dadada@mail.com', 21, 'qwer', 'w')
    #student1 = Student('Bob', 'Bown', 'dadada@mail.com', 25, 'asdasa', 'm')
    dict_st = {'first_name': 'Bob', 'last_name': 'Bown', 'email': 'ghfhfghfg@gmail.com',
               'age': 25, 'address': 'xcvvx', 'gender': 'm', 'point': 0}
    student1 = Student.add_student_dict(dict_st)
    print(student == student1)
    Student.print_total_student()