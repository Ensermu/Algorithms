"""
linked list implementation by adding elements to the first place
"""
class Linked_List(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def Insert(self, t):
        new = Linked(t)
        if self.first is None:
            self.first = new
            self.last = new
        else:
            new.next = self.first
            self.first.previous = new
            self.first = new
        self.length += 1

        return new

    def Search(self, x):
        node = self.first
        while node is not None and x != node.key:
                node = node.next
        return node
    
    def Delete(self, x):
        x = self.Search(x)
        if x.previous is not None:
            x.previous.next = x.next
        else:
            self.first = x.next
        if x.next is not None:
            x.next.previous = x.previous
        self.length -= 1

    def __str__(self):
        elements = []
        temp = self.first
        for i in range(0, self.length):
            elements.append(temp.key)
            temp = temp.next
        
        return str(elements)

class Linked(object):
    def __init__(self, t):
        self.key = t
        self.previous = None
        self.next = None

