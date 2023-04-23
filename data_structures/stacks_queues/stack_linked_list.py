'''
A Stack implementation using a Linked List.
'''


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def print_list(self) -> list:
        array = []
        current_node = self.top
        while current_node:
            array.append(current_node.value)
            current_node = current_node.next
        return array

    def peek(self):
        '''
        See the top element
        '''
        return self.top.value

    def push(self, value):
        '''
        Add a node to the top of the stack
        '''
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        '''
        Remove from the top of the stack
        '''
        if not self.top:
            return None

        if self.top == self.bottom:
            self.bottom = None

        new_top = self.top.next
        self.top = new_top
        self.length -= 1


my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
print(my_stack.peek())
print(my_stack.print_list())
my_stack.pop()
print(my_stack.print_list())
my_stack.pop()
print(my_stack.print_list())
my_stack.pop()
print(my_stack.print_list())
