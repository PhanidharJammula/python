from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def stack_basics():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.container)
    print(s.peek()) # returns last element and not changes container
    print(s.container)
    print(s.pop()) # returns last element and removes it from container
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())
    print(s.container)



if __name__ == '__main__':
    stack_basics()
