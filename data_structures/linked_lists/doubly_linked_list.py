'''
A Doubly Linked List Class
'''


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self) -> list:
        array = []
        current_node = self.head
        while current_node:
            array.append(current_node.value)
            current_node = current_node.next
        return array

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        new_node = Node(value)

        current_node = self.traverse_to_index(index-1)

        holding_pointer = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        holding_pointer.prev = new_node
        new_node.next = holding_pointer
        self.length += 1

    def remove(self, index):

        current_node = self.traverse_to_index(index-1)

        current_node.next.next.prev = current_node
        current_node.next = current_node.next.next

        self.length -= 1


my_doubly_linked_list = DoublyLinkedList()
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(16)
my_doubly_linked_list.prepend(1)
my_doubly_linked_list.insert(2, 99)
print(my_doubly_linked_list.print_list())
my_doubly_linked_list.remove(2)
print(my_doubly_linked_list.print_list())
