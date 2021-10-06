class Task:

    def __init__(self, title):
        self.done = False
        self.title = title
        self._priority = 1

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

class Dashboard:
    def __init__(self):
        self.task_list = []

    def add_task(self):
        title = input('Task name:\t')
        new_task = Task(title)
        self.task_list.append(new_task)


if __name__ == '__main__':
    task = Task('My test task')
    task.priority = 11
    print(task._priority)

