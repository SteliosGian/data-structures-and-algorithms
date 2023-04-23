'''
Implementation of a Queue using Stacks
Example:
queue = MyQueue()
queue.push(1)
queue.push(2)
queue.peek() should return 1
queue.pop() should return 1
queue.empty() should return False
'''


class MyQueue:
    def __init__(self) -> None:
        self.first = []
        self.last = []

    def enqueue(self, value):
        length = len(self.first)
        for i in range(length):
            self.last.append(self.first.pop())
        self.last.append(value)

    def dequeue(self):
        length = len(self.last)
        for i in range(length):
            self.first.append(self.last.pop())
        print(self.first.pop())
        self.first.pop()

    def peek(self):
        if len(self.last) > 0:
            print(self.last[0])
            return self.last[0]
        print(self.first[len(self.first) - 1])
        return self.first[len(self.first) - 1]

    def empty(self):
        if len(self.first) == 0:
            print(False)
            return False
        else:
            print(True)
            return True


queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.peek()
queue.dequeue()
queue.empty()
