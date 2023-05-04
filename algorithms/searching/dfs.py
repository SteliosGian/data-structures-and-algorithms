"""
Depth-First Search Searching Algorithm

      101
33          105

inorder - 33, 101, 105
preorder - 101, 33, 105
postorder - 33, 105, 101
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

    def dfs_inorder(self):
        return self.traverse_inorder(self.root, [])

    def dfs_postorder(self):
        return self.traverse_postorder(self.root, [])

    def dfs_preorder(self):
        return self.traverse_preorder(self.root, [])

    def traverse_inorder(self, node, ls):
        if node.left:
            self.traverse_inorder(node.left, ls)
        ls.append(node.value)

        if node.right:
            self.traverse_inorder(node.right, ls)
        return ls

    def traverse_postorder(self, node, ls):
        if node.left:
            self.traverse_postorder(node.left, ls)

        if node.right:
            self.traverse_postorder(node.right, ls)

        ls.append(node.value)
        return ls

    def traverse_preorder(self, node, ls):
        ls.append(node.value)

        if node.left:
            self.traverse_preorder(node.left, ls)

        if node.right:
            self.traverse_preorder(node.right, ls)
        return ls


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(6)
binary_search_tree.insert(20)
binary_search_tree.insert(170)
binary_search_tree.insert(15)
binary_search_tree.insert(1)
print(binary_search_tree.print_tree())
print(binary_search_tree.dfs_inorder())
print(binary_search_tree.dfs_postorder())
print(binary_search_tree.dfs_preorder())
