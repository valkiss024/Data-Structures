class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        if child in self.children:
            return
        self.children.append(child)

    def remove_child(self, child):
        self.children = [node for node in self.children if node != child]

    def traverse(self):
        nodes_to_visit = [self]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


if __name__ == "__main__":

    root = TreeNode("CEO")

    child_a = TreeNode("General Manager")
    child_b = TreeNode("Marketing Manager")
    child_c = TreeNode("Supervisor")
    child_d = TreeNode("Employee")

    root.add_child(child_a)
    root.add_child(child_b)
    child_a.add_child(child_c)
    child_c.add_child(child_d)

    root.traverse()