class Stack:

    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.array = [0] * stacksize
        self.size = 0

    def Push(self, item):
        if self.IsFull():
            raise Exception('Stack is full')
        self.size += 1
        self.array[self.IndexOfTop()] = item

    def Pop(self):
        if self.IsEmpty():
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop()]
        self.array[self.IndexOfTop()] = 0
        self.size -= 1
        return value

    def Peek(self):
        if self.IsEmpty():
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop()]

    def IsEmpty(self):
        return self.size == 0

    def IsFull(self):
        return self.size == self.stacksize

    def IndexOfTop(self):
        return self.size - 1
