class Open_Addressing(object):
    
    def __init__(self):
        self.m1 = 17
        self.m2 = 8
        self.p = 11
        self.base = 256
        self.storage = self.Build_Table()
        
    def insert(self, key):
        i = 0
        int_key = self.Keys_to_Natural_Numbers(key)
        hash1 = self.Hash_Function1(int_key)
        hash2 = self.Hash_Function2(int_key)
        hash3 = self.Hash_Function3(hash1, hash2, i)
        while True:
          if self.storage[hash3] == None or self.storage[hash3] == 'DeleteMe':
            self.storage[hash3] = key
            return key
          else:
            i += 1
            hash3 = self.Hash_Function3(hash1, hash2, i)
            
    def search(self, key):
        i = 0
        int_key = self.Keys_to_Natural_Numbers(key)
        hash1 = self.Hash_Function1(int_key)
        hash2 = self.Hash_Function2(int_key)
        hash3 = self.Hash_Function3(hash1, hash2, i)
        while True:
          if self.storage[hash3] == None:
              return None
          elif self.storage[hash3] == key:
              return key
          else:
              i += 1
              hash3 = self.Hash_Function3(hash1, hash2, i)
              
    def delete(self, key): 
        i = 0
        int_key = self.Keys_to_Natural_Numbers(key)
        hash1 = self.Hash_Function1(int_key)
        hash2 = self.Hash_Function2(int_key)
        hash3 = self.Hash_Function3(hash1, hash2, i)
        while True:
          if self.storage[hash3] == key:
              self.storage[hash3] = 'DeleteMe'
              return self.storage
          else:
              i += 1
              hash3 = self.Hash_Function3(hash1, hash2, i)
        
    def Keys_to_Natural_Numbers(self, key):
        int_value = 0
        if type(key) == int:
            return key
        power = len(key) - 1
        for i in range(0,len(key)):
            int_value += ord(key[i]) * pow(self.base,power)
            power -= 1
            return int_value
        
    def Hash_Function1(self, key):
        hashed = key % self.m1
        return hashed
    
    def Hash_Function2(self, key):
        hashed = 1 + (key % self.m2)
        return hashed
     
    def Hash_Function3(self, hash1, hash2, i):
        hashed = (hash1 + (i * hash2)) % self.p
        return hashed
    
    def Build_Table(self):
        self.storage = [None] * self.p
        return self.storage
