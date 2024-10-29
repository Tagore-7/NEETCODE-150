#You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.
#
#Return the number of unique paths from the top-left corner of Grid to the bottom-right corner such that all traversed cells are land cells. You may only move vertically or horizontally through land cells. For an individual unique path you cannot visit the same cell twice.
#
#Example 1:
#
#Input: grid = [
#  [0, 0, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 0, 1],
#  [0, 1, 0, 0]
#]
#
#Output:
#2
#

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or (r,c) in visit:
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))
            count = 0
            count += dfs(r + 1, c, visit)
            count += dfs(r - 1, c, visit)
            count += dfs(r, c + 1, visit)
            count += dfs(r, c - 1, visit)

            visit.remove((r,c))
            return count

        return dfs(0, 0, set())

