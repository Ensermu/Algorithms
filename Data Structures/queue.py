class Queue:

    def __init__(self, queuesize):
        self.queuesize = queuesize
        self.array = [0] * queuesize
        self.size = 0

    def Push(self, item):
        if self.IsFull():
            raise Exception('Queue is full')
        self.size += 1
        self.array[self.queuesize - self.IndexOfTop() - 1] = item

    def Pop(self):
        if self.IsEmpty():
            raise Exception('Queue is empty')
        value = self.array[self.IndexOfTop()]
        self.array[self.IndexOfTop()] = 0
        self.size -= 1
        return value

    def Peek(self):
        if self.IsEmpty():
            raise Exception('Queue is empty')
        return self.array[self.IndexOfTop()]

    def IsEmpty(self):
        return self.size == 0

    def IsFull(self):
        return self.size == self.queuesize

    def IndexOfTop(self):
        return self.size - 1
