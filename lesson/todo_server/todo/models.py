import json

from ..utils.binary_search import binary_search_id



# def binary_search_id(array, element, low=None, high=None):
#     if low is None and high is None:
#         low = 0
#         high = len(array) - 1
#
#     if high >= low:
#         mid = (high + low) // 2
#
#         if array[mid].id == element:
#             return array[mid]
#         elif array[mid].id > element:
#             return binary_search_id(array, element, low, mid - 1, )
#         else:
#             return binary_search_id(array, element, mid + 1, high)
#     else:
#         return None


class Task:

    objects = []

    def __init__(self, title, priority=1):
        self.id = len(Task.objects) + 1
        self.done = False
        self.title = title
        self._priority = 1
        self.location = None
        self.tag = None
        self.cildren = []
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

    def add_cild(self, titlle, priority=1):
        cild_task = Task(titlle, priority)
        self.cildren.append(cild_task.id)

    def get_subtasks(self):
        if not self.cildren:
            return []
        children = []
        for children_id in self.cildren:
            child_task = binary_search_id(Task.objects, children_id)
            if child_task is not None:
                children.append(child_task)
                children.extend(child_task.get_subtasks())



if __name__ == '__main__':

    task1 = Task('test1')
    task2 = Task('test2')
    task3 = Task('test3')
    task4 = Task('test4')
    task5 = Task('test5')
    Task.objects.extend([task5, task3, task4, task2, task1])
    print(binary_search_id(Task.objects, 3))
    # # task1.title = 'new test'
    # arr = copy(Task.objects)
    # task2.title = 'sdfghjkljhfgds'
    # for t in Task.objects:
    #     print(t)
    # print('-------------------------------------------------------------')
    # for f in arr:
    #     print(f)
