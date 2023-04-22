'''
Reversed linked list
[1, 10, 16, 88]
should return [88, 16, 10, 1]
'''


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# Singly List List
class LinkedList:
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
            self.head = Node(value)
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
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
        new_node.next = holding_pointer
        self.length += 1

    def remove(self, index):

        current_node = self.traverse_to_index(index-1)

        current_node.next = current_node.next.next

        self.length -= 1

    def reverse(self):

        if not self.head.next:
            return self.head

        first = self.head
        second = first.next

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first


my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(10)
my_linked_list.append(16)
my_linked_list.append(88)
print(my_linked_list.print_list())
my_linked_list.reverse()
print(my_linked_list.print_list())
