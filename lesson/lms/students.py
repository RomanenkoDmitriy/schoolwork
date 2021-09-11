student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mari', 'D', 'adadad@mail.ru', '19', 'Huston', 'F'],
    ['Jon', 's', 'hyhyhyhyh@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'ggggggg@mail.com', 'sexteen', 'Citi', 'M']
]



def add_student():
    student = {}
    for field in student_fields:
        student[field] = input(f'Enter {field}: ')
        if field == 'age':
            try:
                int(student['age'])
            except:
                student['age'] = input('Enter age as number\t')
    STUDENTS.append(student)

def print_student(student):
    for field in student:
        if field.find('_') != -1:
            str_field = f'{field[:field.find("_")]} {field[(field.find("_") + 1):]}'
            print(str_field.capitalize(), '\t', student[field])
        else:
            print(field.capitalize(), '\t', student[field])

def print_student_list():
    for student in STUDENTS:
        print_student(student)
        print('<-------------------------------------------------------->')

def load_students():
    for test_student in TEST_STUDENTS:
        STUDENTS.append(dict(zip(student_fields, test_student)))

def calculate_avg_age():
    try:
        total_age = 0
        for student in STUDENTS:
            total_age += int(student['age'])
        avg_age = total_age / len(STUDENTS)
        print(f'Average age is  {avg_age}')
    except ValueError:
        print('Cannot calculate average age')
    except Exception as e:
        print(str(e))

while True:
    action = input('Desired action:\t')
    if action == 'add':
        add_student()
    elif action == 'age':
        calculate_avg_age()
    elif action == 'load':
        load_students()
    elif action == 'print':
            print_student_list()
    else:
        break