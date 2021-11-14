from random import randint

class TreeNode:

    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None

    def __str__(self):
        return f'data: {self.data}'

    def add(self, data):
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.add(data)
            else:
                self.right = TreeNode(data)

class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root.add(data)

    def contains(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return True
        return False

    def find(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return node
        return None

    def find_closest(self, data):
        node = self.root
        element = []
        val = []
        while node:
            if data < node.data:
                element.append(node)
                val.append((node.data - data))
                node = node.left
            elif data > node.data:
                element.append(node)
                val.append((data - node.data))
                node = node.right
            else:
                return node
        min_val = min(val)
        return element[val.index(min_val)]

    def delete(self, data):
        pass

if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(10):
        tree.add(randint(1, 20))

    print(tree.find_closest(6))