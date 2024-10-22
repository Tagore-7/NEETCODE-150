#Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
#
#LRUCache(int capacity) Initialize the LRU cache of size capacity.
#int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.
#void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
#A key is considered used if a get or a put operation is called on it.
#
#Ensure that get and put each run in 
#O
#(
#1
#)
#O(1) average time complexity.
#
#Example 1:
#
#Input:
#["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
#
#Output:
#[null, null, 10, null, null, 20, -1]
#
#Explanation:
#LRUCache lRUCache = new LRUCache(2);
#lRUCache.put(1, 10);  // cache: {1=10}
#lRUCache.get(1);      // return 10
#lRUCache.put(2, 20);  // cache: {1=10, 2=20}
#lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
#lRUCache.get(2);      // returns 20 
#lRUCache.get(1);      // return -1 (not found)
#Constraints:
#
#1 <= capacity <= 100
#0 <= key <= 1000
#0 <= value <= 1000
#

class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.right = None 

class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nxt = self.right
        self.right.prev = self.left 

    def remove(self, node):
        prev, nxt = node.prev, node.nxt 
        prev.nxt, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt , nxt.prev = node, node
        node.prev, node.nxt = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return  -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

