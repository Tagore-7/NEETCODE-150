from collections import deque

# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# Or use a HashMap
adjList = { "A": [], "B": [] }

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    
    adjList[src].append(dst)

# count paths backtracking dfs 
def dfs(node, target, visit, adjList):
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, visit, adjList)
    visit.remove(node)

    return count 

# shortest path from node to target
def bfs(node, target, visit, adjList):
    queue = deque()
    queue.append(node)
    length = 0

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node == target:
                return length 

            for neighbhor in adjList[node]:
                if neighbhor not in visit:
                    visit.add(neighbhor)
                    queue.append(neighbhor)
        length += 1

    return length

        
