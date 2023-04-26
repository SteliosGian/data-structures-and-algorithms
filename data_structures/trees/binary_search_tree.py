'''
Binary Search Tree
       9
   4       20
1    6   15    170
'''


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

    def remove(self, value):
        if not self.root:
            return None

        current_node = self.root
        parent_node = None

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            elif current_node.value == value:
                # Option 1: No right child
                if not current_node.right:
                    if not parent_node:
                        self.root = current_node.left
                    else:

                        # if parent > current value, make current left child a child of parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        # if parent < current value, make left child a right child of parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left

                # Option 2: Right child which doesn't have a left child
                elif not current_node.right.left:
                    current_node.right.left = current_node.left
                    if not parent_node:
                        self.root = current_node.right
                    else:
                        # if parent > current, make right child of the left the parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right

                        # if parent < current, make right child a right child of the parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                # Option 3: Right child that has a left child
                else:
                    # find the right child's left most child
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left:
                        left_most_parent = left_most
                        left_most = left_most.left

                    # parent's left subtree is not leftmost's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if not parent_node:
                        self.root = left_most
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = left_most
                        elif current_node.value > parent_node.value:
                            parent_node.right = left_most
            return True

    def print_tree(self):
        if self.root is not None:
            self.printt(self.root)

    def printt(self, current_node):
        if current_node is not None:
            self.printt(current_node.left)
            print(str(current_node.value))
            self.printt(current_node.right)


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(6)
binary_search_tree.insert(20)
binary_search_tree.insert(170)
binary_search_tree.insert(15)
binary_search_tree.insert(1)
print(binary_search_tree.print_tree())
