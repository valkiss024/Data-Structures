"""
A CUSTOM HASHMAP IMPLEMENTATION IN PYTHON

This custom HashMap class handles collision by utilizing the open addressing strategy with a probe sequencing of 1

Note: Python has a built-in implementation of hash maps in forms of dictionaries with a more complex functionality
han the custom hash map below!
"""
import string


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for _ in range(self.array_size)]

    def hash(self, key, collision_count):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)

        return hash_code + collision_count

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def get_index_and_value(self, key, collision_count=0):
        index = self.compressor(self.hash(key, collision_count))
        value = self.array[index]

        return index, value

    def retrieve_value_and_index(self, key, collision_count):
        current_index, current_value = self.get_index_and_value(key, collision_count)

        if collision_count > self.array_size or current_value is None:
            return None
        elif current_value[0] == key:
            return current_value[1], current_index
        else:
            return self.retrieve_value_and_index(key, collision_count + 1)

    def insert_value(self, key, collision_count):
        current_index, current_value = self.get_index_and_value(key, collision_count)

        if collision_count > self.array_size:
            return None
        elif current_value is None or current_value[0] == key:
            return current_index
        else:
            return self.insert_value(key, collision_count + 1)

    def set_value(self, key, value):
        current_index, current_value = self.get_index_and_value(key)

        if current_value is None or current_value[0] == key:
            self.array[current_index] = [key, value]
            return
        else:
            collision_count = 1
            new_index = self.insert_value(key, collision_count)
            if new_index is not None:
                self.array[new_index] = [key, value]
                return
            else:
                print("Could not insert - HashMap is full!")
            return

    def get_value(self, key):
        _, current_value = self.get_index_and_value(key)

        if current_value is None:
            return f"No value associated with: '{key}', was found in the HashMap!"
        elif current_value[0] == key:
            return current_value[1]
        else:
            collision_count = 1
            value = self.retrieve_value_and_index(key, collision_count)
            if value is None:
                return f"No value associated with: '{key}', was found in the HashMap!"
            else:
                return value[0]

    def delete_value(self, key):
        current_index, current_value = self.get_index_and_value(key)

        if not current_value:
            print(f"No key with the name: '{key}', was found in the HashMap!")
            return
        elif current_value[0] == key:
            self.array[current_index] = None
            return
        else:
            collision_count = 1
            current_value = self.retrieve_value_and_index(key, collision_count)
            if current_value:
                value, index = current_value
                self.array[index] = None
                return
            else:
                print(f"No key with the name: '{key}', was found in the HashMap!")
            return


if __name__ == "__main__":
    """The alphabet_hash_map maps each ascii lowercase character to its corresponding location in the alphabet
    following: character(key): location in alphabet(value)"""
    alphabet_count = [(letter, index) for index, letter in enumerate(string.ascii_lowercase, 1)]

    alphabet_hash_map = HashMap(len(alphabet_count))
    for element in alphabet_count:
        alphabet_hash_map.set_value(element[0], element[1])

    # UNCOMMENT TO SEE HASH MAP METHODS IN ACTION:

    # print(alphabet_hash_map.get_value("a"))
    # print(alphabet_hash_map.get_value("/"))
    # alphabet_hash_map.delete_value("a")
    # print(alphabet_hash_map.get_value("a"))

    """The languages_hash_map maps each programming language to its developer following: 
    language(key): developer(value)"""

    languages = ["Python", "Java", "C", "C++", "C#", "PHP", "Ruby", "Swift"]
    developers = ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup", "Anders Hejlsberg",
                  "Rasmus Lerdorf", "Yukihiro Matsumoto", "Chris Lattner"]
    langs_and_devs = [(lang, dev) for lang, dev in zip(languages, developers)]

    languages_hash_map = HashMap(len(langs_and_devs) - 1)
    for element in langs_and_devs:
        languages_hash_map.set_value(element[0], element[1])

    # UNCOMMENT TO SEE HASH MAP METHODS IN ACTION:
    # print(languages_hash_map.get_value("Python"))
    # print(languages_hash_map.get_value("Ruby"))
