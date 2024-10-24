#Design a Hash Table class.
#
#Your HashTable class should support the following operations:
#
#HashTable(int capacity) will initialize an empty hash table with a capacity of capacity, where capacity > 1.
#int get(int key) will return the value associated with the key. If the key is not present in the hash table, return -1.
#void insert(int key, int value) will insert the key-value pair into the hash table. If the key is already present in the hash table, the original value should be replaced with the new value.
#bool remove(int key) will remove the key-value pair with the given key. If the key is not present, return false, otherwise return true
#int getSize() will return the number of keys in the hash table.
#int getCapacity() will return the capacity of the hash table.
#void resize() will double the capacity of the hash table. This method should be called automatically when the load factor reaches or exceeds 0.5. Your insert method should automatically call resize() when necessary.
#Note: You can choose how to handle collisions.
#
#Example 1:
#
#Input:
#["HashTable", 4, "insert", 1, 2, "get", 1, "insert", 1, 3, "get", 1, "remove", 1, "get", 1]
#
#Output:
#[null, null, 2, 3, true, -1]
#Example 2:
#
#Input:
#["HashTable", 2, "getCapacity", insert, 6, 7, "getCapacity", "insert", 1, 2, "getCapacity", "insert", 3, 4, "getCapacity", "getSize"]
#
#Output:
#[null, 2, null, 4, null, 8, null, 8, 3]
#
class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = None


class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.hash_table = [None] * self.capacity 
        self.size = 0
    
    def hash_function(self, key):
        return key % self.capacity 

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.hash_table[index]
        
        if node:
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return 
                prev, node = node, node.next 
            prev.next = Node(key, Value)
            self.size += 1
        elif not node:
            self.hash_table[index] = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        node = self.hash_table[self.hash_function(key)]
        
        while  node:
            if node.key == key:
                return node.val 
            node = node.next 
        return -1


    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.hash_table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next 
                else:
                    self.hash_table[index] = node.next
                self.size -= 1
                return True 
            prev, node = node, node.next
        return False 


    def getSize(self) -> int:
        return self.size 

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        newcap = self.capacity * 2
        newtable = [None] * newcap
        
        for node in self.hash_table:
            while node:
                index = key % newcap
                if newtable[index] is None:
                    newtable[index] = Node(node.key, node.val)
                else:
                    new_node = newtable[index]
                    while new_node.next:
                        new_node = new_node.next 
                    new_node.next = Node(node.key, node.val)
                node = node.next 
        self.capacity = newcap
        self.hash_table = newtable



