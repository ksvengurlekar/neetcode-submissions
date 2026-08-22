class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        firstpass = set(nums)
        secondpass = set()
        count = 0

        for i in s:
            if i + 1 in s:
                secondpass.add(i)
                firstpass.remove(i)
            
        for j in firstpass:
            local_count = 1
            while j - 1 in secondpass:
                local_count += 1
                j -= 1
            
            count = max(count, local_count)

        return count
