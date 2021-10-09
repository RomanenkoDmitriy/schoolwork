import unittest
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



    def test_print_tasks_by_priority(self):
        dashboard = Dashboard()
        dashboard.add_task()
        task_priority = dashboard.print_tasks_by_priority()
        self.assertEqual(len(task_priority), 1)


if __name__ == '__main__':
    unittest.main()