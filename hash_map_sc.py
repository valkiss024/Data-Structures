"""
A CUSTOM HASHMAP IMPLEMENTATION IN PYTHON

This custom HashMap class handles collision by utilizing the separate chaining strategy with a custom linked list
being the underlying data structure

Note: Python has a built-in implementation of hash maps in forms of dictionaries with a more complex functionality
han the custom hash map below!
"""
from linked_list import LinkedList


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for _ in range(self.array_size)]

    def hash(self, key):
        """Hash function - returns a hash unique for the key"""
        key_bytes = key.encode()
        hash_code = sum(key_bytes)

        return hash_code

    def compressor(self, hash_code):
        """Using the modulo operator determine a valid array index"""
        return hash_code % self.array_size

    def get_list_and_index(self, key):
        index = self.compressor(self.hash(key))
        linked_list_ = self.array[index]

        return linked_list_

    def set_value(self, key, value):
        linked_list_ = self.get_list_and_index(key)

        for node in linked_list_:
            if node.get_value()[0] == key:
                node.get_value()[1] = value
        else:
            linked_list_.insert_to_head([key, value])

    def get_value(self, key):
        linked_list_ = self.get_list_and_index(key)

        for node in linked_list_:
            if node.get_value()[0] == key:
                return node.get_value()[1]
        else:
            return f"No key with the name: '{key}', was found in the HashMap!"

    def delete_value(self, key):
        linked_list = self.get_list_and_index(key)

        previous_node = None
        current_node = linked_list.get_head_node()

        while current_node:
            if current_node.get_value()[0] == key:
                if current_node == linked_list.get_head_node():
                    linked_list.head_node = current_node.get_next_node()
                    break
                else:
                    previous_node.set_next_node(current_node.get_next_node())
                    break
            previous_node = current_node
            current_node = current_node.get_next_node()
        else:
            print(f"No value with the key: '{key}, was found in the HashMap!'")

        return

if __name__ == "__main__":
    """The languages_hash_map maps each programming language to its developer following: 
       language(key): developer(value)"""

    languages = ["Python", "Java", "C", "C++", "C#", "PHP", "Ruby", "Swift"]
    developers = ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup", "Anders Hejlsberg",
                  "Rasmus Lerdorf", "Yukihiro Matsumoto", "Chris Lattner"]
    langs_and_devs = [(lang, dev) for lang, dev in zip(languages, developers)]

    languages_hash_map = HashMap(5)
    for element in langs_and_devs:
        languages_hash_map.set_value(element[0], element[1])

    # UNCOMMENT TO SEE HASH MAP METHODS IN ACTION:
    # print(languages_hash_map.get_value("Python"))
    # print(languages_hash_map.get_value("Ruby"))

    # languages_hash_map.delete_value("Java")
    # languages_hash_map.delete_value("Kotlin")
    # languages_hash_map.delete_value("Java")
