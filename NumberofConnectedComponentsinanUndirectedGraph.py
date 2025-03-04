#There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
#
#The nodes are numbered from 0 to n - 1.
#
#Return the total number of connected components in that graph.
#
#Example 1:
#
#Input:
#n=3
#edges=[[0,1], [0,2]]
#
#Output:
#1
#Example 2:
#
#Input:
#n=6
#edges=[[0,1], [1,2], [2,3], [4,5]]
#
#Output:
#2
#Constraints:
#
#1 <= n <= 100
#0 <= edges.length <= n * (n - 1) / 2
#
class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n 
    
    def find(self, node):
        curr = node
        while curr != self.par[curr]:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr 
    
    def union(self, n1, n2):
        p1 , p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False 

        if self.rank[p1] > self.rank[p2]:
            p1, p2 = p2, p1 
        
        self.par[p2] = p1 
        self.rank[p1] += self.rank[p2]

        return True 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n 
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res
        
