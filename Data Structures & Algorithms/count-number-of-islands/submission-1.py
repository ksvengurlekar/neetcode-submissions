from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(x, y):
            q = deque([(x, y)])
            while q:
                a, b = q.popleft()
                for dx, dy in dirs:
                    nx, ny = a+dx, b+dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == "1":
                        q.append((nx, ny))
                    
                visited[a][b] = True

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1

        return count
                        
