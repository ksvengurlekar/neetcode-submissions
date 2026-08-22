from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxarea = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def bfs(r, c):
            q = deque([(r, c)])
            local_a = 1
            visited.add((r, c))

            while q:
                x, y = q.popleft()
                for i, j in dirs:
                    new_row, new_col = x + i, y + j
                    if not (0 <= new_row < n) or not (0 <= new_col < m) or (new_row, new_col) in visited or grid[new_row][new_col] == 0:
                        continue

                    local_a += 1
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))

            return local_a

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxarea = max(maxarea, bfs(i, j))

        return maxarea
