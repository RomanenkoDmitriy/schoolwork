
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
        if email[0] != '@' and email[-1] != '@' and '@' in email:
            self._email = email
        else:
            raise AttributeError('Invalid email')
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






if __name__ == '__main__':
    student = Student('Mari', 'Boow', 'dadada@mail.com', 21, 'qwer', 'w')
    #student.email = 'dadadda@mdsd'
    print(student.email)