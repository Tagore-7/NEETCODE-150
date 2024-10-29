#You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
#
#An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
#
#The area of an island is defined as the number of cells within the island.
#
#Return the maximum area of an island in grid. If no island exists, return 0.
#
#Example 1:
#
#
#
#Input: grid = [
#  [0,1,1,0,1],
#  [1,0,1,0,1],
#  [0,1,1,0,1],
#  [0,1,0,0,1]
#]
#
#Output: 6
#Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.
#
#Constraints:
#
#1 <= grid.length, grid[i].length <= 50
#
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visit = set()
        DIRS = [(0 , 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                r, c = q.popleft()
                for i, j in DIRS:
                    nr, nc = r + i, c + j
                    if (nr in range(ROWS) and
                       nc in range(COLS) and
                       grid[nr][nc] == 1 and
                       (nr, nc) not in visit):
                       area += 1
                       q.append((nr, nc))
                       visit.add((nr, nc))
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    newArea =  bfs(r, c)
                    maxArea = max(maxArea , newArea)
        return maxArea

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visit = set()
        # DIRS = [(0 , 1), (1, 0), (0, -1), (-1, 0)]

        # def bfs(r, c):
        #     area = 1
        #     q = deque()
        #     q.append((r, c))
        #     visit.add((r, c))
        #     while q:
        #         r, c = q.popleft()
        #         for i, j in DIRS:
        #             nr, nc = r + i, c + j
        #             if (nr in range(ROWS) and 
        #                nc in range(COLS) and 
        #                grid[nr][nc] == 1 and 
        #                (nr, nc) not in visit):
        #                area += 1
        #                q.append((nr, nc))
        #                visit.add((nr, nc))
        #     return area 
        def dfs(r, c):
            if (
                r < 0 or 
                c < 0 or 
                r == ROWS or
                c  == COLS or 
                grid[r][c] == 0 or 
                (r,c) in visit
            ):
                return 0

            visit.add((r, c))

            return  1 + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r +1, c) + dfs(r , c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                # if grid[r][c] == 1 and (r, c) not in visit:
                #     newArea =  bfs(r, c)
                #     maxArea = max(maxArea , newArea)
                maxArea = max(maxArea, dfs(r, c))
        return maxArea
