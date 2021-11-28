import unittest
import os

from lesson33 import FileManage

class FileManagerTest(unittest.TestCase):

    file_manager = FileManage()

    def test_del_file_dir(self):
        self.file_manager.del_file_dir('test.txt')
        self.assertEqual(len(self.file_manager.del_file_list), 1)

    def test_print_tree_dir(self):
        self.file_manager.print_tree_dir()
        self.assertTrue((len(self.file_manager.dict_dir) > 0))

    def test_new_dir(self):
        self.file_manager.new_dir('test_dir')
        self.assertIn('test_dir', os.listdir(os.path.join(os.getcwd())))

    def test_rename_dir(self):
        self.file_manager.rename_dir('test_dir', 'test_dir2')
        self.assertIn('test_dir2', os.listdir(os.path.join(os.getcwd())))

    def test_del_dir(self):
        self.file_manager.del_dir('test_dir2')
        self.assertNotIn('test_dir2', os.listdir(os.path.join(os.getcwd())))

    def test_new_file(self):
        self.file_manager.new_file('test2.txt')
        self.assertIn('test2.txt', os.listdir(os.path.join(os.getcwd())))

    def test_rename_file(self):
        self.file_manager.rename_file('test2.txt', 'test3.txt')
        self.assertIn('test3.txt', os.listdir(os.path.join(os.getcwd())))

    def test_move_file(self):
        self.file_manager.move_file('test3.txt', 'test_dir3')
        self.assertIn('test3.txt', os.listdir(os.path.join(os.getcwd(), 'test_dir3')))

    def test_del_file(self):
        self.file_manager.del_file('test.txt')
        self.assertNotIn('test.txt', os.listdir(os.path.join(os.getcwd())))





if __name__ == '__main__':
    unittest.main()