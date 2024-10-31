#Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
#
#A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#
#All the visited cells of the path are 0.
#All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
#The length of a clear path is the number of visited cells of this path.
#
# 
#
#Example 1:
#
#
#Input: grid = [[0,1],[1,0]]
#Output: 2
#Example 2:
#
#
#Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
#Output: 4
#Example 3:
#
#Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
#Output: -1
# 
#
#Constraints:
#
#n == grid.length
#n == grid[i].length
#1 <= n <= 100
#grid[i][j] is 0 or 1
#
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        visit =  set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 1
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[-1, 0], [-1, +1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for i, j in DIRS:
                    nr, nc = r + i, c + j
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1

        return -1

