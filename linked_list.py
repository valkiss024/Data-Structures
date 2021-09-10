"""
CUSTOM LINKED LIST IMPLEMENTATION IN PYTHON

The custom LinkedList class contains the following methods:
    * __init__  --> class constructor
    * __len__  --> returns the length of the linked list when 'len()' is called
    * __iter__  --> turns the linked list into an iterator object (able to traverse it using a for loop)
    * __add__  --> overloading the '+' operator, allowing concatenating two linked lists

    * reverse  --> A classic implementation of reversing a linked list
    * reverse_with_recursion  --> reversing the linked list using recursion
    * reverse_with_stack  --> reversing the linked list using a stack

"""

from node import Node
from stack import Stack


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current_node = self.head_node

        while current_node:
            yield current_node
            current_node = current_node.get_next_node()

    def __add__(self, other_linked_list):
        current_tail = self.find_nth_last(1)
        other_current = other_linked_list.get_head_node()

        while other_current:
            current_tail.set_next_node(other_current)
            current_tail = other_current
            other_current = other_current.get_next_node()

    def reverse(self):
        current = self.head_node
        prev = None

        while current:
            next_node = current.get_next_node()
            current.set_next_node(prev)
            prev = current
            current = next_node
        self.head_node = prev

    def reverse_with_recursion(self):
        if self.head_node is None:
            return
        self.recursion_reverse(self.head_node, None)

    def recursion_reverse(self, current, prev):
        if current.get_next_node() is None:
            self.head_node = current

            current.set_next_node(prev)
            return

        next_node = current.get_next_node()
        current.set_next_node(prev)

        self.recursion_reverse(next_node, current)

    def reverse_with_stack(self):
        stack = Stack(self.length)

        current_node = self.head_node
        while current_node.get_next_node():
            stack.push(current_node.get_value())
            next_node = current_node.get_next_node()
            current_node = next_node

        self.head_node = current_node
        while not stack.is_empty():
            next_node = stack.pop()
            current_node.set_next_node(next_node)
            current_node = next_node

        current_node.set_next_node(None)

    def get_head_node(self):
        return self.head_node

    def insert_to_head(self, new_value):
        new_node = Node(new_value, self.head_node)
        self.head_node = new_node
        self.length += 1

    def delete_value(self, value):
        previous_node = None
        current_node = self.head_node

        while current_node:
            if current_node.get_value() == value:
                if current_node == self.head_node:
                    self.head_node = current_node.get_next_node()
                    self.length -= 1
                    break
                else:
                    previous_node.set_next_node(current_node.get_next_node())
                    self.length -= 1
                    break
            previous_node = current_node
            current_node = current_node.get_next_node()
        else:
            print(f"'{value}' not found!")

    def value_at(self, index):
        current_node = self.head_node
        current_index = 0

        if not isinstance(index, int):
            raise TypeError(f"{type(index)} was found instead of type 'int'")

        while current_node:
            if current_index == index:
                return current_node.get_value()
            current_node = current_node.get_next_node()
            current_index += 1
        else:
            raise IndexError("Index was not found!")

    def index_of(self, value):
        current_node = self.head_node
        current_index = 0

        while current_node:
            if current_node.get_value() == value:
                return current_index
            current_node = current_node.get_next_node()
            current_index += 1
        else:
            return f"No such value as: '{value}'"

    def middle_value(self):
        """Two pointers to traverse the list, one is twice as fast as the other"""
        fast_pointer = self.head_node
        slow_pointer = self.head_node
        count = 0

        while fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            if count % 2 != 0:
                slow_pointer = slow_pointer.get_next_node()
            count += 1

        return slow_pointer.get_value()

    def find_nth_last(self, index):
        if not isinstance(index, int):
            raise TypeError(f"{type(index)} was found instead of 'int'")
        if index > self.length or index <= 0:
            raise IndexError("Index out of range!")
        item_index = self.length - index
        current_index = 0
        current_node = self.head_node

        while current_index != item_index:
            current_node = current_node.get_next_node()
            current_index += 1

        return current_node

    def stringify_list(self):
        current_node = self.head_node
        while current_node:
            print(current_node.get_value())
            current_node = current_node.get_next_node()


# Creating two LinkedList objects for testing

values_1 = ["Python", "Classes", "Data structures", "Algorithms", "Functions"]
values_2 = [1, 2, 3, 4, 5]
my_linked_list_1 = LinkedList()
my_linked_list_2 = LinkedList()
for i in range(len(values_1)):
    my_linked_list_1.insert_to_head(values_1[i])
    my_linked_list_2.insert_to_head(values_2[i])

if __name__ == "__main__":

    # UNCOMMENT TO SEE LINKED LISTS' METHODS IN ACTION:

    print("--- ORIGINAL LIST ---\n")
    my_linked_list_1.stringify_list()

    print("\n\n--- REVERSE METHOD ---\n")
    my_linked_list_1.reverse()
    my_linked_list_1.stringify_list()

    print("\n\n--- RECURSION REVERSE METHOD ---\n")
    my_linked_list_1.reverse_with_recursion()
    my_linked_list_1.stringify_list()

    print("\n\n--- STACK REVERSE METHOD ---\n")
    my_linked_list_1.reverse_with_stack()
    my_linked_list_1.stringify_list()

    print("\n\n--- DELETE METHOD ---\n")
    my_linked_list_1.delete_value("Python")
    my_linked_list_1.stringify_list()

    print("\n\n--- FIND A VALUE BY INDEX ---\n")
    print(my_linked_list_1.value_at(0))

    print("\n\n--- FIND THE INDEX OF A VALUE ---\n")
    print(my_linked_list_1.index_of("Python"))

    print("\n\n--- FIND THE MIDDLE VALUE ---\n")
    print(my_linked_list_1.middle_value())

    print("\n\n--- FIND THE NTH LAST ITEM ---\n")
    print(my_linked_list_1.find_nth_last(1).get_value())

    print("\n\n--- ADD TWO LINKED LIST TOGETHER ---\n")
    my_linked_list_1 + my_linked_list_2
    my_linked_list_1.stringify_list()
