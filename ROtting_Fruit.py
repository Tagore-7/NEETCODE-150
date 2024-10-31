#You are given a 2-D matrix grid. Each cell can have one of three possible values:
#
#0 representing an empty cell
#1 representing a fresh fruit
#2 representing a rotten fruit
#Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.
#
#Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
#
#Example 1:
#
#
#
#Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
#
#Output: 4
#Example 2:
#
#Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
#
#Output: -1
#Constraints:
#
#1 <= grid.length, grid[i].length <= 10
#
class Solution:
    def orangeRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for r in range(ROWS):
            for j in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for i , j in DIRS:
                    nr , nc = i + r, j + c 
                    if min(nr, nc) < 0 or r == ROWS or c == COLS or grid[nr][nc] != 1:
                        continue 
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            time += 1

        return time if not fresh else -1
