class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    # This method will be called when we try to set obj[key]=val
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))

# This method will be called when we try to get val from obj[key]
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]


    def __delitem__(self,key):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]

hash=HashTable()
hash['march 6']=120
hash['march 6']=78
hash['march 8']=67
hash['march 9']=4
hash['march 17']=459

print(hash.arr)
print(hash['march 17'])
del hash['march 17']
print(hash.arr)
