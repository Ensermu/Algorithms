import random

class Skip_List:
    def __init__(self):
        self.first = [node(float('-inf'))]
        self.level = 0
        self.n = 0
        
    def Insert(self, x):
        new = cluster()
        new.level.append(node(x))
        if self.n == 0:
            self.first[self.level].next = new.level[self.level]
            new.level[self.level].prev = self.first[self.level]
        else:
            current = self.first[self.level]
            n = self.level
            while True:
                if current.next is None and n == 0:
                    current.next = new.level[n]
                    new.level[n].prev = current
                    break
                elif n == 0 and x < current.next.value and x > current.value:
                    current.next.prev = new.level[n]
                    current.next, new.level[n].next = new.level[n], current.next
                    new.level[n].prev = current
                    break
                elif current.next is None or current.next.value > x:
                    current = current.down
                    n -= 1
                else:
                    current = current.next
        self.n += 1
        n = 0
        while True:
            rand = random.randint(0, 1)
            if rand:
                n += 1
                new.level.append(node(x))
                if n > self.level:
                    Node = node(float('-inf'))
                    self.first.append(Node)
                    self.level += 1
                    Node.down = self.first[self.level-1]
                    self.first[self.level-1].top = Node
                else:
                    current = new.level[n-1]
                    while True:
                        if current.prev.top is not None:
                            Node = current.prev.top
                            break
                        current = current.prev
                Node.next = new.level[n]
                new.level[n].prev = Node
                new.level[n].down = new.level[n-1]
                new.level[n-1].top = new.level[n]
            else:
                break

    def Search(self, x): 
        n = self.level
        current = self.first[n]
        while True:
            if n < 0:
                return False
            elif current.next is None and n == 0:
                return False
            elif current.next is None and n != 0:
                current = current.down
                n -= 1
            elif current.next.value == x:
                return True
            elif current.next.value < x:
                current = current.next
            elif current.next.value > x:
                current = current.down
                n -= 1
    
class node:
    def __init__(self, x):
        self.value = x
        self.prev = None
        self.next = None
        self.top = None
        self.down = None

class cluster:
    def __init__(self):
        self.level = []