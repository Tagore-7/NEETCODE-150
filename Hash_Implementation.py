class Pair:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 

class Hash:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 2
        self.map = [None, None]

    def hash(self, key: int):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity 

    def get(self, key: int):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity 
       return None 

   def put(self, key: int, val: int):
       index = self.hash(key)

       while True:
           if self.map[index] == None:
               self.map[index] = Pair(key, val)
               self.size += 1
               if self.size > self.capacity // 2:
                   self.rehash()
               return 
           elif self.map[index].key == key:
               self.map[index].val = val
               return 
           index += 1
           index = index % self.capacity 

   def remove(self, key: int):
       index = self.hash(key)

       while True:
           if self.map[index].key == key:
               self.map[index] = None 
               self.size -= 1
               return 
           index += 1
           index = index % capacity 
   
   def rehash(self):
       self.capacity = 2 * self.capacity 
       newMap = [None] * self.capacity 
       oldmap = self.map
       self.map = newMap 
       self.size = 0
       for pair in oldmap:
           if pair:
               self.map.put(Pair(key, val))
  
   def print(self):
       for pair in self.map:
           if pair:
               print(pair.key, pair.val)
