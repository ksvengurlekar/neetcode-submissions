class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row, col):
            q = deque([(row, col)])
            
            while q:
                r, c = q.popleft()
                for i, j in dirs:
                    newrow, newcol = r+i, c+j
                    if not (0 <= newrow < n) or not (0 <= newcol < m) or grid[newrow][newcol] < grid[r][c] + 1:
                        continue
                    
                    grid[newrow][newcol] = grid[r][c] + 1
                    q.append((newrow, newcol))
                        
        
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 0:
                    bfs(x, y)
                