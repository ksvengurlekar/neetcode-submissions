from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        n, m = len(grid), len(grid[0])
        rottime = {}

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    q.append([r, c, 0])
                    rottime[r*100 + c] = 0
                elif grid[r][c] == 1:
                    rottime[r*100 + c] = 1001
                else:
                    rottime[r*100 + c] = 0

        while q:
            x, y, t = q.popleft()
            for dx, dy in dirs:
                r, c = x+dx, y+dy

                if 0 <= r < n and 0 <= c < m and grid[r][c] > 0 and rottime[r*100 + c] > t + 1:
                    rottime[r*100 + c] = t+1
                    q.append([r,c,t+1])


        ret = max(rottime.values())
        return ret if ret < 1001 else -1