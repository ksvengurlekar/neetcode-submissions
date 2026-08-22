class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i, x in enumerate(nums):
            if x > 0:
                break
            
            if i > 0 and x == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                v = nums[l] + nums[r] + x
                if v < 0:
                    l += 1
                elif v > 0:
                    r -= 1
                else:
                    sol.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return sol