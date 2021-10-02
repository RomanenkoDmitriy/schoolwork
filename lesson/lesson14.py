# пациент, водитель, студент, клиент магазина, робочий

class Person:
    def __init__(self, last_name, first_name, age, email):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.email = email


class Patient(Person):

    list_medications = []

    def __init__(self, date_posting, discharge_date, diagnosis):
        self.date_posting = date_posting
        self.discharge_date = discharge_date
        self.diagnosis = diagnosis

    def treatment(self, medications):
        self.list_medications.append(medications)

    def discharge(self, date):
        self.discharge_date = date



class Driver(Person):
    def __init__(self, driving_experience, category, health_status=True):
        self.driving_experience = driving_experience
        self.category = category
        self.health_status = health_status


class Student(Person):
    def __init__(self, course, average_score):

        self.course = course
        self.average_score = average_score


class ShopClient(Person):
    order = {}

    def __init__(self, average_purchase_amount, discount=0):

        self.average_purchase_amount = average_purchase_amount
        self.discount = discount

    def checkout(self):
        name = input('Enter product name:\t')
        number = input('Enter number:\t')
        self.order[name] = number

class Emplyer(Person):

    def __init__(self, experience, salary):

        self.experience = experience
        self.salary = salary