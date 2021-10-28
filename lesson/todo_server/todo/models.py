import json
from copy import copy
class Task:

    objects = []

    def __init__(self, title, priority=1):
        self.id = len(Task.objects) + 1
        self.done = False
        self.title = title
        self._priority = 1
        self.location = None
        self.tag = None
        Task.objects.append(self)

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Task(title=\'{}\')'.format(self.title)

    # def __copy__(self):
    #     task_copy = type(self)(self.title)
    #     task_copy.__dict__.update(self.__dict__)
    #     return task_copy

    @property
    def priority(self):
        return self._priority

    @priority.setter    
    def priority(self, value):
        if value in range(1, 11):
            self._priority = value
        else:
            raise ValueError('Priority value is out of range')

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def get_list(cls):
        return cls.objects

    @classmethod
    def list_to_json(cls):
        task_list = [t.__dict__ for t in cls.objects]
        return json.dumps(task_list)


# task1 = Task('test1')
# task2 = Task('test2')
# task3 = Task('test3')
# task4 = Task('test4')
# task5 = Task('test5')
# task1.title = 'new test'
# arr = copy(Task.objects)
# task2.title = 'sdfghjkljhfgds'
# for t in Task.objects:
#     print(t)
# print('-------------------------------------------------------------')
# for f in arr:
#     print(f)
