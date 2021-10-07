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

    def print_all_tasks(self):
        for task in self.task_list:
            return task

    def print_tasks_by_priority(self):
        task_priority = []
        inp_priority = int(input('Enter priority:\t'))

        for task in self.task_list:
            print(task)
            print(task.priority)
            if task.priority == inp_priority:
                task_priority.append(task)

        return task_priority




if __name__ == '__main__':
    task = Task('My test task')
    dashboard = Dashboard()
    dashboard.add_task()
    dashboard.task_list[-1].priority = 2
    print(dashboard.task_list[-1].priority)
    dashboard.add_task()
    dashboard.task_list[-1].priority = 2
    dashboard.add_task()
    dashboard.task_list[-1].priority = 4
    print(dashboard.print_tasks_by_priority())
    #dashboard.print_all_tasks()
    #task.priority = 11
    #print(task._priority)
    # out = str(task)
    # print(out)

