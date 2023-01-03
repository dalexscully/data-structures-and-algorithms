import pytest
from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):

        if self.stack1.is_empty():
            raise Exception("PseudoQueue is Empty")

        while not self.stack1.is_empty():
            popped = self.stack1.pop()
            self.stack2.push(popped)

        dequed = self.stack2.pop()

        while not self.stack2.is_empty():
            popped = self.stack2.pop()
            self.stack1.push(popped)

        return dequed

    def is_empty(self):
        return self.stack1.is_empty()

    if __name__ == "__main__":
        pass
