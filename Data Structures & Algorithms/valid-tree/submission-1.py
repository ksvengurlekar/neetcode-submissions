'''
n = 3
[[0, 1], [0, 2] [1, 2]]

set = 0 2 3 1
stack =   

  0
 / \
1 - 2
     \
      3

'''

from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        if not edges:
            return True

        hm = defaultdict(list)
        for v1, v2 in edges:
            hm[v1].append(v2)
            hm[v2].append(v1)

        visited = set()
        stack = deque([(edges[0][0], -1)])

        while stack:
            node, parent = stack.pop()

            if node in visited:
                return False

            visited.add(node)
            for connecting in hm[node]:
                if connecting == parent:
                    continue

                stack.append((connecting, node))
        
        return len(visited) == n

