class Rolling_Hash(object):

    def __init__(self, s):
        self.HASH_BASE = 10
        self.seqlen = len(s)
        self.p = 17
        n = self.seqlen - 1
        h = 0
        for c in s:
            h += ord(c) * (self.HASH_BASE ** n)
            n -= 1
        self.curhash = h%self.p 

    def current_hash(self):
        return self.curhash

    def slide(self, previtm, nextitm):
            self.curhash = (self.curhash * self.HASH_BASE) + ord(nextitm)
            self.curhash -= ord(previtm) * (self.HASH_BASE ** self.seqlen)
            self.curhash = self.curhash%self.p
            return self.curhash
            
def Karp_Rabin(s, text):
    j = 0
    rs = Rolling_Hash(s)
    rt = Rolling_Hash(text[0:len(s)])
    if rs.current_hash() == rt.current_hash():
    	if s == text:
        	print('found match')
    for i in range(len(s), len(text)):
        rt.slide(text[i-len(s)], text[i])
        if rs.current_hash() == rt.current_hash():
            j += 1
            if s == text[i - len(s) + 1:i+1]:
                print('found match')
                print('collisions:', j)

