'''
A Stack implementation using an Array.
'''


class Stack:
    def __init__(self) -> None:
        self.array = []

    def __str__(self) -> str:
        return str(self.array)

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        self.array.pop()


my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
print(my_stack.peek())
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
