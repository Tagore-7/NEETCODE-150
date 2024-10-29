#Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
#
#An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
#
#Example 1:
#
#Input: grid = [
#    ["0","1","1","1","0"],
#    ["0","1","0","1","0"],
#    ["1","1","0","0","0"],
#    ["0","0","0","0","0"]
#  ]
#Output: 1
#Example 2:
#
#Input: grid = [
#    ["1","1","0","0","1"],
#    ["1","1","0","0","1"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]
#  ]
#Output: 4
#Constraints:
#
#1 <= grid.length, grid[i].length <= 100
#grid[i][j] is '0' or '1'.
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS,COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            while queue:
                r, c = queue.popleft()
                for i, j in DIRS:
                    nr, nc = r + i, c + j
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1" and (nr, nc) not in visit:
                         queue.append((nr, nc))
                         visit.add((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands

