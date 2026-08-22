class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        top, bottom = 0, n - 1
        while top <= bottom:
            midrow = (top + bottom) // 2
            if target > matrix[midrow][-1]:
                top = midrow + 1
            elif target < matrix[midrow][0]:
                bottom = midrow - 1
            else:
                break

        if top > bottom:
            return False

        midrow = (top + bottom) // 2
        l, r = 0, m - 1
        while l <= r:
            midcol = (l + r) // 2
            if target > matrix[midrow][midcol]:
                l = midcol + 1
            elif target < matrix[midrow][midcol]:
                r = midcol - 1
            else:
                return True

        return False 
