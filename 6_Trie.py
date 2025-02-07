# Trie (Prefix Implementation)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False 

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                curr.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True 

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.chilren:
                return False 
            cur = cur.children[c]
        return cur.word 

    def startsWith(Self, prefix):
        curr = self.root 
        for p in prefix:
            if p not in curr.children:
                return False 
            curr = curr.children[c]

        return True 

