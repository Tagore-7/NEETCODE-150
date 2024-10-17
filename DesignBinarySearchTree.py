#Design a Binary Search Tree class.
#
#You will design a Tree Map, which maps an integer key to an integer value. Your Tree class should support the following operations:
#
#TreeMap() will initialize an binary search tree map.
#void insert(int key, int val) will map the key to the value and insert it into the tree.
#int get(int key) will return the value mapped with the key. If the key is not present in the tree, return -1.
#int getMin() will return the value mapped to the smallest key in the tree. If the tree is empty, return -1.
#int getMax() will return the value mapped to the largest key in the tree. If the tree is empty, return -1.
#void remove(int key) will remove the key-value pair with the given key from the tree.
#int[] getInorderKeys() will return an array of the keys in the tree in ascending order.
#Note:
#
#The tree should be ordered by the keys.
#The tree should not contain duplicate keys. If the key is already present in the tree, the original key-value pair should be overridden with the new key-value pair.
#Example 1:
#
#Input:
#["insert", 1, 2, "get", 1, "insert", 4, 0, "getMin", "getMax"]
#
#Output:
#[null, 2, null, 2, 0]
#Example 2:
#
#Input:
#["insert", 1, 2, "insert", 4, 2, "insert", 3, 7, "insert", 2, 1, "getInorderKeys", "remove", 1, "getInorderKeys"]
#
#Output:
#[null, null, null, null, [1, 2, 3, 4], null, [2, 3, 4]]
#

class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    def __init__(self):
        self.root = None 

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not root:
            self.root = newNode 
            return 
        
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return 
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return 
                curr = curr.right
            else:
                curr.val = val
                return 

    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if curr.key == key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right 
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1 
        curr = self.root

        while curr.left:
            curr = curr.left
        return curr.val 
    
    def getMax(self):
        if not self.root:
            return -1
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key) -> None:
        self.root = self._remove_helper(self.root, key)

    def _remove_helper(self, root, key):
        if not root:
            return None

        if key < root.key:
            self._remove_helper(root.left, key)
        elif key > root.key:
            self._remove_helper(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMinNode(root)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self._remove_helper(root.right, minNode.key)
        return root

    def findMinNode(self, root):
        if not self.root:
            return None 
        curr = root

        while curr.left:
            curr = curr.left
        return curr

    def getInOrderKeys(self) -> List[int]:
        values = []
        self.inorder(self.root, values)
        return values

    def inorder(self, root, values):
        if not root:
            return 
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)






















        
                 

