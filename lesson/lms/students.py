import json
import csv

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender', 'point']

STUDENTS = []

TEST_STUDENTS = [
    ['Mari', 'D', 'adadad@mail.ru', '19', 'Huston', 'F', 0],
    ['Jon', 's', 'hyhyhyhyh@mail.com', '21', 'London', 'M', 0],
    ['Andy', 'H', 'ggggggg@mail.com', 'sexteen', 'Citi', 'M', 0]
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
        print(field.replace('_', ' ').capitalize(), '\t', student[field])

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

def dump_students():
    with open('data/student_data.json', 'w') as file:
        json.dump(STUDENTS, file)

def load_from_json(file_path='data/student_data.json'):
    with open(file_path, 'r') as file:
        STUDENTS.extend(json.load(file))

def dump_csv():
    with open('data/student_data.csv', 'w') as file:
        writer = csv.DictWriter(file, student_fields)
        writer.writeheader()
        for studetn in STUDENTS:
            writer.writerow(studetn)

def load_csv(file_path='data/student_data.csv'):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            STUDENTS.append(row)




ACTIONS = {
    'add': add_student,
    'age': calculate_avg_age,
    'load': load_students,
    'print': print_student_list,
    'dump_json': dump_students,
    'load_json': load_from_json,
    'dump_csv': dump_csv,
    'load_csv': load_csv

}
if __name__ == '__main__':
    while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
            ACTIONS.get(action)()
        else:
            break
