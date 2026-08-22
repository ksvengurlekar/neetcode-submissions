from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        count = 0
        visited = set()
        nrows, ncols = len(grid), len(grid[0])

        def bfs(r, c):
            frontier = deque()
            visited.add((r, c))
            frontier.append((r, c))

            while frontier:
                row, col = frontier.popleft()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if (r in range(nrows) and c in range(ncols) and (r, c) not in visited and grid[r][c] == "1"):
                        frontier.append((r, c))
                        visited.add((r, c))

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    count += 1

        return count