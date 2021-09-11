student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mari', 'D', 'adadad@mail.ru', '19', 'Huston', 'F'],
    ['Jon', 's', 'hyhyhyhyh@mail.com', '21', 'London', 'M']
]



def add_student():
    student = {}
    for field in student_fields:
        student[field] = input(f'Enter {field}: ')
    STUDENTS.append(student)

def print_student(student):
    for field in student:
        print(field.capitalize(), '\t', student[field])

def load_students():
    for  test_student in TEST_STUDENTS:
        student = {}
        for index in range(len(student_fields)):
            student[student_fields[index]] = test_student[index]

    STUDENTS.append(student)



while True:
    action = input('Desired action:\t')
    if action == 'add':
        add_student()
    elif action == 'load':
        load_students()
    elif action == 'print':
        for student in STUDENTS:
            print_student(student)
    else:
        break