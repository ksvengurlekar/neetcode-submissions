class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j = len(nums)-k+1
        result = []
        for i in range(j):
            result.append(max(nums[i:i+k]))
        
        return result