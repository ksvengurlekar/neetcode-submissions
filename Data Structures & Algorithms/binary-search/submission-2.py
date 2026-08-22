class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def mid(left: int, right: int) -> int:
            return left + (right - left) // 2

        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = mid(l, r)
                
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
            
        return -1