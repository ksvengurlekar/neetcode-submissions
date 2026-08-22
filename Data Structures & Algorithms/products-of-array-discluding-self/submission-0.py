class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left  = [1] * n
        right = [1] * n

        for l in range(1, n):
            left[l] = left[l-1] * nums[l-1]
            right[n-l-1] = right[n-l] * nums[n-l]
        
        return [left[i]*right[i] for i in range(n)]