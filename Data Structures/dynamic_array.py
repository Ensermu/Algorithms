class DynamicArray:
    def __init__(self):
        self._items = [None]
        self._n = 0

    def __len__(self):
        return self._n

    def __iter__(self):
        for i in range(self._n):
            yield self._items[i]

    def _rebuild(self, n):
        temp = [None] * n
        for i in range(self._n):
            temp[i] = self._items[i]
        self._items = temp

    def at(self, i):
        return self._items[i]

    def set(self, i, x):
        self._items[i] = x

    def insert_right(self, x):
        if self._n == len(self._items):
            self._rebuild(2 * self._n)
        self._items[self._n] = x
        self._n += 1

    def delete_right(self):
        if self._n < 1:
            raise IndexError('pop from empty list')
        if 4 * self._n < len(self._items):
            self._rebuild(2 * self._n)
        self._n -= 1
        
    def __str__(self):                  
        return str(self._items)
