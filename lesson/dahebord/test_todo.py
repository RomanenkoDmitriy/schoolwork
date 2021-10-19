import unittest
import io
from unittest.mock import patch
from lesson17 import Task, Dashboard


class TestTask(unittest.TestCase):

    def test_task_object(self):
        task = Task('My test task')
        self.assertEqual(task.title, 'My test task')
        self.assertFalse(task.done)

    def test_dashboard_object(self):
        dashboard = Dashboard()
        self.assertIsInstance(dashboard.task_list, list)
        self.assertEqual(len(dashboard.task_list), 0)

    @patch('builtins.input', return_value='My test task')
    def test_add_task(self, mock_input):
        dashboard = Dashboard()
        dashboard.add_task()
        self.assertEqual(len(dashboard.task_list), 1)
        self.assertEqual(dashboard.task_list[0].title, 'My test task')

    def test_get_task_priority(self):
        task = Task('My test task')
        self.assertEqual(task.priority, 1)

    def test_get_task_correct_priority(self):
        task = Task('My test task')
        task.priority = 5
        self.assertEqual(task.priority, 5)

    def test_get_task_incorrect_priority(self):
        task = Task('My test task')
        task.priority = 20
        self.assertEqual(task.priority, 1)

    def test_task_str(self):
        task = Task('My test task')
        output = str(task)
        self.assertEqual(output, 'My test task')

    @patch('builtins.input', return_value='My test task')
    def test_print_all_task(self, mock_input):
        dashboard = Dashboard()
        dashboard.add_task()
        self.assertEqual(str(dashboard.print_all_tasks()), 'My test task')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_all_tasks(self, mock_stdout):
        task1 = Task('My test task')
        task2 = Task('My second task')
        dashboard = Dashboard()
        dashboard.task_list.extend([task1, task2])
        dashboard.print_all_tasks()
        self.assertEqual(mock_stdout.getvalue(),
                         'My test task\nMy second task\n')

    def test_tag_object(self):
        task = Task('My test task')
        self.assertIsNone(task.tag, None)

    @patch('builtins.input', return_value='Task1')
    def test_title_search(self, mock_input):
        task = Task('Task1')
        task2 = Task('Task2')
        dashboard = Dashboard()
        dashboard.task_list.extend([task, task2])
        self.assertNotEqual(len(dashboard.title_search()), 0)

    @patch('builtins.input', return_value='tag')
    def test_tag_search(self, mock_input):
        task = Task('Task1', 'tag')
        task2 = Task('Task2', 'tag1')
        dashboard = Dashboard()
        dashboard.task_list.extend([task, task2])
        self.assertNotEqual(len(dashboard.tag_search()), 0)

    @patch('builtins.input', return_value='tag')
    def test_completed_task(self, mock_input):
        task1 = Task('Task1', 'tag')
        task1.done = True
        task2 = Task('Task2', 'tag1')
        dashboard = Dashboard()
        dashboard.task_list.extend([task1, task2])
        for task in dashboard.completed_task():
            self.assertEqual(task, task1)

    def test_sort_by_priority(self):
        task = Task('My test task')
        task.priority = 2

        task1 = Task('My test task1')
        task1.priority = 3

        task2 = Task('My test task2')
        task2.priority = 4

        dashboard = Dashboard()
        dashboard.task_list.extend([task1, task2, task])

        self.assertEqual(dashboard.sort_by_priority(), [task, task1, task2])

    def test_dump_to_json(self):
        task1 = Task('D task')
        task2 = Task('A task')
        dashboard = Dashboard()
        dashboard.task_list.extend([task1, task2])
        dashboard.dump_to_json()


    def test_dump_task_csv(self):
        task1 = Task('D task')
        task2 = Task('A task')
        dashboard = Dashboard()
        dashboard.task_list.extend([task1, task2])
        dashboard.dump_task_csv()

    def test_load_from_json(self):
        dashboard = Dashboard()
        self.assertNotEqual(len(dashboard.load_from_json()), 0)

    def test_load_from_csv(self):
        dashboard = Dashboard()
        self.assertNotEqual(len(dashboard.load_from_csv()), 0)

    # @patch('builtins.input', return_value=3)
    # def test_print_priority(self, mock_input):
    #     task = Task('My test task')
    #     task.priority = 2
    #
    #     task1 = Task('My test task1')
    #     task1.priority = 3
    #
    #     task2 = Task('My test task2')
    #     task2.priority = 3
    #
    #     dashboard = Dashboard()
    #     dashboard.task_list.extend([task1, task2, task])
    #     self.assertEqual(len(dashboard.print_tasks_by_priority()), 2)



if __name__ == '__main__':
    unittest.main()