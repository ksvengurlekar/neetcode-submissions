class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = abs(nums[i])
            nums[x-1] *= -1

            if nums[x-1] > 0:
                return x

        return -1
