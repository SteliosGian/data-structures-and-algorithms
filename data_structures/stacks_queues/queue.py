'''
A Queue implementation
'''


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def print_list(self) -> list:
        array = []
        current_node = self.first
        while current_node:
            array.append(current_node.value)
            current_node = current_node.next
        return array

    def peek(self):
        return self.first.value

    def enqueue(self, value):
        '''
        Add to queue
        '''
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        '''
        Remove from the front of the list
        '''
        if not self.first:
            return None

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.length -= 1


my_queue = Queue()
my_queue.enqueue('Joy')
print(my_queue.print_list())
my_queue.enqueue('Matt')
print(my_queue.print_list())
my_queue.enqueue('Pavel')
print(my_queue.print_list())
my_queue.enqueue('Samir')
print(my_queue.print_list())
my_queue.dequeue()
print(my_queue.print_list())
