#You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.
#
#Return the length of the shortest path from the top-left corner of Grid to the bottom-right corner such that all traversed cells are land cells. You may only move vertically or horizontally through land cells.
#
#Note:
#
#If there is no such path, return -1.
#The length of a path is the number of moves from the starting cell to the ending cell.
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
#6
#
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [1, 0], [0, -1], [-1 ,0]]
        length = 0
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



