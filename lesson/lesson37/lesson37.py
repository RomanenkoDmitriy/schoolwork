# З використанням будь-яких зручних інструментів, створити програму, яка дозволяє планувати робочий час спеціалістів (наприклад, лікарів).
# Програма має зберігати інформацію про робочі дні спеціаліста протягом наступного тижня - кожен день може бути робочим чи вихідним,
# у робочі дні спеціаліст має робочі години (наприклад, понеділок-п'ятниця прийом з 9:00 до 18:00, субота та неділя - вихідні).
# Протягом робочого дня спеціаліст приймає клієнтів (пацієнтів), що записані до нього.
# Кожен прийом триває годину та починається на початку години (наприклад, з 9:00 до 10:00 Іванов, з 10:00 до 11:00 Сидоренко, з 12:00 до 13:00 Петров).
# Програма має надавти можливість шукати вільні "вікна" у лікаря на тиждень (у попередньому прикладі - з 11:00 до 12:00),
# створювати запис для пацієнта на обраний час (якщо цей час вільний), переносити запис на інший вільний час або до іншого лікаря, скасовувати запис.
# Усі дані (розклад роботи лікарів, заплановані записи тощо) програма має зберігати у JSON файлах,
# які мають оновлюватися при кожній зміні інформації. На початку роботи програма, за наявності торрібних файлів,
# має завантажувати усі раніше створені дані.
#
# Після написання програми створіть 10 тестових спеціалістів (лікарів) з їхнім розкладом роботи. Створіть функцію,
# яка додаватиме певну кількість записів до цих спеціалістів (кількість передається цій функції як аргумент, кожен запис виконується на перше вільне вікно,
# прізвище пацієнта будь-яке, можна рандомний рядок). Задекоруйте її декоратором, який засікатиме час виконання функції. Створіть 10, 100, 1000 записів.
# За результатами виводу оцініть час, необхідний для створення одного запису у кожному випадку

import json
from datetime import datetime
import os

# datetime.today().weekday()


class DaySpecialist:

    def __init__(self, now_day):
        self.now_day = now_day
        if self.now_day in ['Mon', 'Tue', 'Wed', 'Thr', 'Fri']:
            self.work_day = True
        else:
            self.work_day = False
        self.time_work = list(range(8, 18))

    def __str__(self):
        return f'{self.work_day} {self.now_day} {self.time_work}'

    @classmethod
    def obj_day(cls, dict_day):
        obj = cls(now_day=None)
        for key, val in dict_day.items():
            setattr(obj, key, val)
        return obj


class Specialist:

    def __init__(self, name):
        self.name = name
        self.work_week = {'Mon': DaySpecialist('Mon'), 'Tue': DaySpecialist('Tue'), 'Wed': DaySpecialist('Wed'), 'Thr': DaySpecialist('Thr'),
                          'Fri': DaySpecialist('Fri'), 'Sat': DaySpecialist('Sat'), 'San': DaySpecialist('San')}
        self.visitor = {}

    def dump_json_work_week(self):
        path_file = os.path.join(os.getcwd(), 'data', f'{self.name}.json')
        dict_week = {k: v.__dict__ for k, v in self.work_week.items()}
        with open(path_file, 'w') as file:
            json.dump(dict_week, file)

    def dump_visitor_json(self, visit_dict):
        path = os.path.join(os.getcwd(), 'data', f'{self.name}_visitor.json')
        with open(path, 'w') as file:
            json.dump(visit_dict, file)

    def recording_for_approx(self, name, day_visit, time_visit):
        path = os.path.join(os.getcwd(), 'data')
        path_file = os.path.join(os.getcwd(), 'data', f'{self.name}.json')
        path_visit = os.path.join(os.getcwd(), 'data', f'{self.name}_visitor.json')

        day = None

        if f'{self.name}.json' not in os.listdir(path):
            day = self.work_week[day_visit]
            day.now_day = day_visit
        else:
            with open(path_file, 'r') as file:
                dict_days = {k: DaySpecialist.obj_day(v) for k, v in json.load(file).items()}
                day = dict_days[day_visit]
                day.now_day = day_visit

        if f'{self.name}_visitor.json' in os.listdir(path):
            with open(path_visit, 'r') as file:
                self.visitor = json.load(file)

        if day.work_day and time_visit in day.time_work:
            self.visitor[name] = [day_visit, day.time_work.pop(day.time_work.index(time_visit))]
            print('Ok')
            print(day.time_work)
            self.work_week[day_visit] = day
            self.dump_json_work_week()
            self.dump_visitor_json(self.visitor)
        elif day.work_day and time_visit not in day.time_work:
            print(f'Work time {day.time_work} or else day')
        elif not day.work_day:
            print('Weekend, please choose other day')


if __name__ == '__main__':
    spec = Specialist('Bob')

    # spec.dump_json_work_week()
    spec.recording_for_approx('Joi', 'Wed', 10)
    print(spec.visitor)
    spec.recording_for_approx('Mark', 'Fri', 10)
    print(spec.visitor)
    spec.recording_for_approx('Lui', 'Mon', 10)
    print(spec.visitor)
    spec.recording_for_approx('Lysi', 'Mon', 10)
    print(spec.visitor)
    spec.recording_for_approx('L', 'Mon', 12)
    print(spec.visitor)
    spec.recording_for_approx('Lv', 'Mon', 14)
    print(spec.visitor)
    # for i in spec.work_week:
    #     print(i)
    # print(day.date)
    # print(day.now_day)

    # spec.work_days(5)
    # spec.recording_for_approx('Joi', 'Wed', 10)
    # # print(spec.visitor)
    #
    # for i in spec.work:
    #     print(i)