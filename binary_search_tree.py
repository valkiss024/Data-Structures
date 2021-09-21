import random


class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value, self.depth + 1)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value, self.depth + 1)
            else:
                self.right.insert(value)

    def traverse(self):
        """Binary search tree traversal with depth-first search --> output the values in ascending order"""
        if self.left:
            self.left.traverse()
        print(f"Value - {self.value}, Depth - {self.depth}")
        if self.right:
            self.right.traverse()

    def find(self, value):
        if self.value == value:
            return f"{value} found at depth: {self.depth}"
        elif value < self.value and self.left:
            return self.left.find(value)
        elif value >= self.value and self.right:
            return self.right.find(value)
        else:
            return f"{value} was not found in the search tree!"

    def delete(self, value):
        if self.value > value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif self.value < value:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            if not self.right:
                return self.left
            elif not self.left:
                return self.right
            else:
                successor_parent, successor = self.right.find_successor(self)

                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right

                successor.left = self.left
                successor.right = self.right

                return successor

        return self

    def find_successor(self, parent):
        if self.left:
            return self.left.find_successor(self)
        else:
            return [parent, self]


if __name__ == "__main__":

    root = BinarySearchTree(50)

    to_find = 75
    root.insert(to_find)
    for _ in range(10):
        random_numb = random.randint(0, 100)
        root.insert(random_numb)

    root.traverse()

    root.delete(75)
    print("AFTER DELETE:")
    root.traverse()
