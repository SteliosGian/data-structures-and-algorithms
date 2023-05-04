"""
Breadth-First Search Searching Algorithm
       9
   4       20
1    6   15    170
"""


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        if not self.root:
            return None
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
        return None

    def print_tree(self):
        if self.root is not None:
            self.printt(self.root)

    def printt(self, current_node):
        if current_node is not None:
            self.printt(current_node.left)
            print(str(current_node.value))
            self.printt(current_node.right)

    def breadth_first_search(self) -> list:
        current_node = self.root
        ls = []
        queue = []

        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            ls.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return ls

    def breadth_first_search_recursive(self, queue: list, ls: list) -> list:
        if len(queue) == 0:
            return ls
        current_node = queue.pop(0)
        ls.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.breadth_first_search_recursive(queue, ls)


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(6)
binary_search_tree.insert(20)
binary_search_tree.insert(170)
binary_search_tree.insert(15)
binary_search_tree.insert(1)
print(binary_search_tree.print_tree())
print(binary_search_tree.breadth_first_search())
print(binary_search_tree.breadth_first_search_recursive([binary_search_tree.root], []))
