
class Student:

    #student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender', 'point']
    TOTAL_STUDENT = []

    def __init__(self, first_name, last_name, email, age, address, gender, point=0):
        self. first_name = first_name
        self. last_name = last_name
        self.age = age
        self. address = address
        self.gender = gender
        self.point = point
        self.email = email
        # if email[0] != '@' and email[-1] != '@' and '@' in email:
        #     self._email = email
        # else:
        #     raise AttributeError('Invalid email')
        Student.TOTAL_STUDENT.append({self.first_name: self})


    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    @classmethod
    def print_total_student(cls):
        print(cls.TOTAL_STUDENT)

    @classmethod
    def add_student_dict(cls, dict_student):
        obj = cls(first_name='', last_name='', email='', age=0, address='', gender='', point=0)
        for key in dict_student:
            setattr(obj, key, dict_student[key])
        return obj

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email[0] != '@' and email[-1] != '@' and '@' in email:
            self._email = email
        else:
            raise AttributeError('Invalid email')


class Group:

    def __init__(self, name):
        self.name = name
        self.STUDENTS = []

    def __iter__(self):
        self.index_student = 0
        return self

    def __next__(self):
        if self.index_student < len(self.STUDENTS):
            _index = self.index_student
            self.index_student += 1
            return self.STUDENTS[_index]
        else:
            raise StopIteration


    def add_student_to_group(self, *args):
        for student in args:
            self.STUDENTS.append(student)

#         В каком варианте лучьше реализововать добовление студентов в группу?

    # def add_student_to_group(self, *args):
    #     for student in Student.TOTAL_STUDENT:
    #         self.STUDENTS.append(student)

    def print_student_list(self):
        for student in self.STUDENTS:
            print(student)
            print('<-------------------------------------------------------->')






if __name__ == '__main__':
    student = Student('Mari', 'Boow', 'dadada@mail.com', 21, 'qwer', 'w')
    student1 = Student('Joi', 'Boow', 'dadada@mail.com', 22, 'qwer', 'm')
    student2 = Student('Bob', 'Boow', 'dadada@mail.com', 20, 'qwer', 'm')
    student3 = Student('Mik', 'Boow', 'dadada@mail.com', 23, 'qwer', 'm')
    student4 = Student('Ann', 'Boow', 'dadada@mail.com', 22, 'qwer', 'w')

    group = Group('beetroot')

    group.add_student_to_group(student, student1, student2, student3, student4)

    iter_group = iter(group)
    for student in iter_group:
        print(student)
    #group.print_student_list()
