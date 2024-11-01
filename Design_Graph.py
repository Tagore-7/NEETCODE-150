Class Graph:
    def __init__(self):
        self.adjList = set()

    def addEdge(self, src: int,dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False 
        self.adjList[src].remove(dst)
        return True 
    
    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)

    def dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True 
        
        visited.add(src)
        for neighbor in self.adjList.get(src, []):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True 
        return False 

    def bfs(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque()
        queue.append([src])
        
        while queue:
            node = queue.popleft()
            if node == dst:
                return True
            visit.add(node)
            for neighbor in self.adjList.get(src, []):
                if neighbor not in visit:
                    queue.append(neighbor)
                    visit.add(neighbor)
        return False 
