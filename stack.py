from node import Node


class Stack:
    def __init__(self, max_size=None):
        self.top_item = None
        self.size = 0
        self.max_size = max_size

    def push(self, new_value):
        if self.has_space():
            new_item = Node(new_value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
        else:
            print("Stack is full!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove
        else:
            print("Stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Stack is empty!")

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        if self.max_size:
            return self.size < self.max_size
        return True
