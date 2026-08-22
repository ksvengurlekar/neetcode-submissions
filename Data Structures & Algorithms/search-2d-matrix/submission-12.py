class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, (r*c) - 1

        while l <= r:
            m = (l + r) >> 1
            v = matrix[m // c][m % c]

            if v == target:
                return True

            if v < target:
                l = m + 1
            else:
                r = m - 1

        return False