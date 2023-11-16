import sys

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert_left(self,key):
        t = BinaryTree(key)
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t 

    def insert_right(self,key):
        t = BinaryTree(key)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t 

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    @property
    def min_value(self):
        return self._find_min(self)

    def _find_min(self, current_node):
        if current_node is None:
            return float('None')
        min_val = current_node.key
        if current_node.left:
            left_min = self._find_min(current_node.left)
            min_val = min(min_val, left_min)
        if current_node.right:
            right_min = self._find_min(current_node.right)
            min_val = min(min_val, right_min)
        return min_val

    def __str__(self):
        return f"[{self.key}; {self.left}; {self.right}]"

def main():
    r = BinaryTree('1')
    print(r)
    r.insert_left('2')
    print(r)
    r.get_left_child().insert_right('3')
    r.get_left_child().get_right_child().insert_left('4')
    r.get_left_child().get_right_child().insert_right('5')
    print(r)
    r.set_root_val('9')
    print(r)

    print("Minimum value in the tree:", r.min_value)

if __name__ == '__main__':
    sys.exit(main())
