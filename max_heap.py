import random


class MaxHeap:
    def __init__(self):
        self.heap_array = [None]
        self.count = 0

    def is_empty(self):
        return True if self.count == 0 else False

    def get_root_node(self):
        return self.heap_array[1] if len(self.heap_array) > 1 else None

    def get_last_node(self):
        return self.heap_array[self.count]

    def get_all(self):
        return self.heap_array[1:]

    @staticmethod
    def left_child_index(parent_index):
        return parent_index * 2

    @staticmethod
    def right_child_index(parent_index):
        return (parent_index * 2) + 1

    @staticmethod
    def parent_index(child_index):
        return child_index // 2

    def add(self, element):
        self.heap_array.append(element)
        self.count += 1
        self.heapify_up()

    def heapify_up(self):
        idx = self.count  # find the index of the last node
        while self.parent_index(idx) > 0:
            parent_idx = self.parent_index(idx)
            child_value = self.heap_array[idx]
            parent_value = self.heap_array[parent_idx]

            if child_value > parent_value:
                self.heap_array[parent_idx], self.heap_array[idx] = child_value, parent_value

            idx = parent_idx

    def has_child(self, idx):
        return self.left_child_index(idx) <= self.count

    def calculate_larger_child_idx(self, idx):
        if self.right_child_index(idx) > self.count:  # if right child does not exists
            return self.left_child_index(idx)  # return left child

        right_child_value = self.heap_array[self.right_child_index(idx)]
        left_child_value = self.heap_array[self.left_child_index(idx)]

        if right_child_value > left_child_value:
            return self.right_child_index(idx)
        else:
            return self.left_child_index(idx)

    def retrieve_max(self):
        if self.count == 0:
            return None
        else:
            max_value = self.heap_array[1]
            self.heap_array[1] = self.heap_array[self.count]
            self.heap_array.pop()
            self.count -= 1
            self.heapify_down()
            return max_value

    def delete(self):
        if self.count == 0:
            print("Heap is empty!")
        else:
            self.heap_array[1] = self.heap_array[self.count]  # replace the first value with the last node
            self.heap_array.pop()
            self.count -= 1
            if self.count > 0:
                self.heapify_down()

    def heapify_down(self):
        idx = 1
        while self.has_child(idx):
            larger_child_idx = self.calculate_larger_child_idx(idx)
            parent_value = self.heap_array[idx]
            child_value = self.heap_array[larger_child_idx]
            if child_value > parent_value:
                self.heap_array[idx], self.heap_array[larger_child_idx] = child_value, parent_value
            else:
                break

            idx = larger_child_idx


if __name__ == "__main__":

    max_heap = MaxHeap()

    for _ in range(10):
        max_heap.add(random.randint(1, 101))

    print(max_heap.get_all())

    for _ in range(12):
        max_heap.delete()
