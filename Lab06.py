import unittest
from Lab05 import BinaryTree  

class TestBinaryTree(unittest.TestCase):
    def test_insert_left(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        self.assertEqual(tree.get_left_child().get_root_val(), 2, "The return value is wrong")

    def test_insert_right(self):
        tree = BinaryTree(1)
        tree.insert_right(3)
        self.assertEqual(tree.get_right_child().get_root_val(), 3, "The return value is wrong")

    def test_get_left_child(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        self.assertEqual(tree.get_left_child().get_root_val(), 2, "The return value is wrong")

    def test_get_right_child(self):
        tree = BinaryTree(1)
        tree.insert_right(3)
        self.assertEqual(tree.get_right_child().get_root_val(), 3, "The return value is wrong")

    def test_set_root_val(self):
        tree = BinaryTree(1)
        tree.set_root_val(4)
        self.assertEqual(tree.get_root_val(), 4, "The return value is wrong")
        
    def test_str(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        tree.insert_right(3)
        self.assertEqual(str(tree), "[1; [2; None; None]; [3; None; None]]", "The return value is wrong")

if __name__ == '__main__':
    unittest.main()