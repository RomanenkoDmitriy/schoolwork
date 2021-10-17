import csv
import json
import os
from datetime import datetime
import googlemaps


class OpenFile:

    def __init__(self, filename, mode):
        self._file = open(filename, mode)

    def __enter__(self):
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        return True

class Maps:

    def __init__(self, key=''):
        self._key = key
        self.gmaps = googlemaps.Client(self._key)

    def __enter__(self):
        return self.gmaps

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.gmaps
        return True

# Додати поле tag (тег) для Task, значення за замовчанням - None
class Task:

    def __init__(self, title, tag=None):
        self.done = False
        self.title = title
        self._priority = 1
        self.tag = tag
        self.location = None

    def __str__(self):
        return f'{self.title.capitalize()}'

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        if priority in range(1, 11):
            self._priority = priority
        else:
            return 'Value out of range'

    # def add_location(self):
    #     place_lookup = input('Enter location name: \t')
    #     gmaps = googlemaps.Client(
    #         key='AIzaSyCSa5JPQryMFDOWmT-_4ZeFZb-SEDxFyiA')
    #     try:
    #         place = gmaps.find_place(
    #             place_lookup,
    #             'textquery',
    #             fields=['geometry/location', 'name', 'place_id']
    #         )
    #         if place['status'] == 'OK':
    #             self.location = {
    #                 'coordinates': place['candidates'][0]['geometry']['location'],
    #                 'name': place['candidates'][0]['name'],
    #                 'google_id': place['candidates'][0]['place_id']
    #             }
    #         else:
    #             raise RuntimeError('Cannot set location')
    #     except:
    #         return

    def add_location(self):
        place_lookup = input('Enter location name: \t')
        with Maps() as gmaps:
            place = gmaps.find_place(
                place_lookup,
                'textquery',
                fields=['geometry/location', 'name', 'place_id']
            )
            if place['status'] == 'OK':
                self.location = {
                    'coordinates': place['candidates'][0]['geometry']['location'],
                    'name': place['candidates'][0]['name'],
                    'google_id': place['candidates'][0]['place_id']
                }
            else:
                raise RuntimeError('Cannot set location')

class Dashboard:

    def __init__(self):
        self.task_list = []

    def add_task(self):
        title = input('Task name:\t')
        new_task = Task(title)
        self.task_list.append(new_task)

    def print_all_tasks(self):
        for task in self.task_list:
            print(task)

    def print_tasks_by_priority(self):
        task_priority = []
        inp_priority = int(input('Enter priority:\t'))

        for task in self.task_list:
            print(task)
            print(task.priority)
            if task.priority == inp_priority:
                task_priority.append(task)

        return task_priority

    #У Dashboard додати можливість пошуку за Task title
    def title_search(self):
        title = input('Enter title:\t')
        title_list = []
        for task in self.task_list:
            if task.title == title:
                title_list.append(task)
        return title_list

    #У Dashboard додати можливість пошуку задачі за Task tag
    def tag_search(self):
        tag = input('Enter tag:\t')
        tag_list = []
        for task in self.task_list:
            if task.tag == tag:
                tag_list.append(task)
        return tag_list

    #У Dashboard додати можливість вивести список завершених задач(done == True) по заданому tag
    def completed_task(self):
        t_list = Dashboard.tag_search(self)
        completed_list = []
        for task in t_list:
            if task.done == True:
                completed_list.append(task)
        return completed_list

    def sort_by_priority(self):
        return sorted(self.task_list, key=lambda task: task.priority)

    def dump_to_json(self):
        filename = f'tasks_{datetime.now().strftime("%Y%m%d%H%M%S")}.json'
        filepath = os.path.join(os.getcwd(), 'data', filename)
        task_list = [task.__dict__ for task in self.task_list]
        with OpenFile(filepath, 'w') as file:
            json.dump(task_list, file)

    def dump_task_csv(self):
        filename = f'tasks_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
        filepath = os.path.join(os.getcwd(), 'data', filename)
        task_list = [task.__dict__ for task in self.task_list]
        with OpenFile(filepath, 'w') as file:
            writer = csv.DictWriter(file, [dict_task.keys() for  dict_task in task_list][0])
            writer.writeheader()
            for dict_task in task_list:
                writer.writerow(dict_task)

    def load_from_json(self):
        dirpath = os.path.join(os.getcwd(), 'data')
        files_data = os.listdir(dirpath)
        filepath = os.path.join(os.getcwd(), 'data',
                                [file for file in files_data if file.endswith('json')][-1])

        task_list = []
        with OpenFile(filepath, 'r') as file:
            task_list.extend(json.load(file))

        return task_list

    def load_from_csv(self):
        dirpath = os.path.join(os.getcwd(),'data')
        files_data = os.listdir(dirpath)
        filepath = os.path.join(os.getcwd(), 'data',
                                [file for file in files_data if file.endswith('csv')][-1])

        task_list = []
        with OpenFile(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_list.append(row)

        return task_list






if __name__ == '__main__':
    task = Task('My test task')
    task.done = True
    task.priority = 4

    task1 = Task('My test task1', '#task1')
    task1.done = True

    task2 = Task('My test task2', '#task1')
    task2.priority = 3

    task3 = Task('My test task3', '#task3')
    task3.done = True
    task3.priority = 3

    task4 = Task('My test task4', '#task2')
    task4.priority = 2

    dashboard = Dashboard()
    dashboard.task_list.extend([task, task1, task2, task3, task4])

    # dashboard.dump_to_json()
    # dashboard.dump_task_csv()
    # print(dashboard.load_from_json())
    # print(dashboard.load_from_csv())
    # print(dashboard.load_from_json())

    # for task in dashboard.sort_by_priority():
    #     print(task)

    # dashboard.add_task()
    # dashboard.task_list[-1].priority = 2
    # print(dashboard.task_list[-1].priority)
    # dashboard.add_task()
    # dashboard.task_list[-1].priority = 2
    # dashboard.add_task()
    # dashboard.task_list[-1].priority = 4
    # print(dashboard.print_tasks_by_priority())
    # dashboard.print_all_tasks()
    # task.priority = 11
    # print(task._priority)
    # out = str(task)
    # print(out)

