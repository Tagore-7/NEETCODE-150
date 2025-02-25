#Design a special dictionary that searches the words in it by a prefix and a suffix.
#
#Implement the WordFilter class:
#
#WordFilter(string[] words) Initializes the object with the words in the dictionary.
#f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
# 
#
#Example 1:
#
#Input
#["WordFilter", "f"]
#[[["apple"]], ["a", "e"]]
#Output
#[null, 0]
#Explanation
#WordFilter wordFilter = new WordFilter(["apple"]);
#wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
# 
#
#Constraints:
#
#1 <= words.length <= 104
#1 <= words[i].length <= 7
#1 <= pref.length, suff.length <= 7
#words[i], pref and suff consist of lowercase English letters only.
#At most 104 calls will be made to the function f.
#
class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word, i):
        curr = self.root

        for ch in word:
            ind = ord(ch) - ord("a")
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.index = i

    def search(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                return -1
            curr = curr.children[index]
        return curr.index



class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.char = '{'

        for i, w in enumerate(words):
            w_len = len(w)
            for j in range(w_len):
                suffix = w[j:]
                for k in range(w_len + 1):
                    prefix = w[: k]
                    self.trie.addWord(suffix + self.char + prefix, i )



    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(suff + self.char + pref)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
