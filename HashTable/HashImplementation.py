class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    # This method will be called when we try to set obj[key]=val
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val

# This method will be called when we try to get val from obj[key]
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

hash=HashTable()
hash['march 6']=130
hash['march 1']=130
hash['dec 6']=130
print(hash['march 6'])
