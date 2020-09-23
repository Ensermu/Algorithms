import random
class Perfect_Hash(object):
    
    def __init__(self, k):
        self.m = k
        self.p = 17
        self.base = 256
        self.a = random.randint(0, self.p - 1)
        self.b = random.randint(1, self.p - 1)
        self.storage = self.Build_Table()
        
    def insert(self, key):
        int_key = self.Keys_to_Natural_Numbers(key)
        hash_value = self.Hash_Function(int_key)
        if self.storage[hash_value] is None:
            index_address = Node()
            index_address.elements.append(key)
            self.storage[hash_value] = index_address
        else:
            self.storage[hash_value].elements.append(key)
                       
    def search(self,key):
        int_key = self.Keys_to_Natural_Numbers(key)
        hash_value = self.Hash_Function(int_key)
        if self.storage[hash_value].m == 0:
            return False
        hash_value1 = self.Hash_Function1(int_key, self.storage[hash_value].a, self.storage[hash_value].b, self.storage[hash_value].m)         
        if self.storage[hash_value].storage[hash_value1] != None and key in self.storage[hash_value].storage[hash_value1].elements:
            print(self.storage[hash_value].storage[hash_value1].elements)
            return True
        else:
            return False
        
    def Keys_to_Natural_Numbers(self, key):
        int_value = 0
        if type(key) == int:
            return key
        power = len(key) - 1
        for i in range(len(key)):
            int_value += ord(key[i]) * (self.base ** power)
            power -= 1
        return int_value
        
    def Hash_Function(self, key):
        hashed = (((self.a) * key + self.b) % self.p) % self.m
        return hashed
    def Hash_Function1(self, k, a, b, m):
        hashed = (((a) * k + b) % self.p) % m
        return hashed
    def Build_Table(self):
        self.storage = [None] * self.m
        return self.storage

class Node:
    def __init__(self):
        self.elements = []

def perfect_hash(A):
    for i in range(len(A.storage)):
        if A.storage[i] is None:
            k = 0
        else:
            k = len(A.storage[i].elements)**2
        A.storage[i], b = Perfect_Hash(k), A.storage[i]
        if b is not None:
            for j in b.elements:
                A.storage[i].insert(j)