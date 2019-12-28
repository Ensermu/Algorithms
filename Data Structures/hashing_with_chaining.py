import random
import linked_list as linked
class Hash_with_Chaining(object):
    
    def __init__(self):
        self.m = 8
        self.p = 17
        self.base = 256
        self.a = random.randint(0, self.p - 1)
        self.b = random.randint(1, self.p - 1)
        self.storage = self.Build_Table()
        
    def insert(self, key):
        int_key = self.Keys_to_Natural_Numbers(key)
        hash_value = self.Hash_Function(int_key)
        if self.storage[hash_value] is None:
            index_address = linked.Linked_List()
            index_address.Insert(key)
            self.storage[hash_value] = index_address
        else:
            self.storage[hash_value].Insert(key)
                       
    def search(self,key):
        int_key = self.Keys_to_Natural_Numbers(key)
        hash_value = self.Hash_Function(int_key)
        if self.storage[hash_value].Search(key) is None:
            return 'not found'
        else:
            return self.storage[hash_value].Search(key).key
        
    def delete(self,key):
        int_key = self.Keys_to_Natural_Numbers(key)
        hash_value = self.Hash_Function(int_key)
        if self.storage[hash_value].Search(key) is not None: 
            self.storage[hash_value].Delete(key)
        
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
    
    def Build_Table(self):
        self.storage = [None] * self.m
        return self.storage
        
